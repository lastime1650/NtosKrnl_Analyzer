# PsChargeProcessQuota

- RVA: `0x0047DEC0`–`0x0047DEEF` (길이 `47` bytes)
- VA: `0x000000014047DEC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `13`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0047DEE0` → [PspChargeQuota](../39/PspChargeQuota_function_00390330.md) (function, `0x00390330`)

### Direct callers
- [MmAdjustWorkingSetSizeEx](MmAdjustWorkingSetSizeEx_function_0047D8D4.md) at `0x0047DC2D`
- [MmCreateProcessAddressSpace](../../page/A5/MmCreateProcessAddressSpace_function_00A5EE5C.md) at `0x00A5EFF7`

### Static image references
- `0x0047DEC4` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047DEC0  48 83 EC 28                     sub rsp, 0x28
0047DEC4  48 3B 0D E5 8B B4 00            cmp rcx, qword ptr [rip + 0xb48be5]
0047DECB  48 8B D1                        mov rdx, rcx
0047DECE  74 1B                           je 0x14047deeb
0047DED0  48 8B 89 F8 02 00 00            mov rcx, qword ptr [rcx + 0x2f8]
0047DED7  4D 8B C8                        mov r9, r8
0047DEDA  41 B8 03 00 00 00               mov r8d, 3
0047DEE0  E8 4B 24 F1 FF                  call 0x140390330
0047DEE5  48 83 C4 28                     add rsp, 0x28
0047DEE9  C3                              ret
0047DEEA  CC                              int3
0047DEEB  33 C0                           xor eax, eax
0047DEED  EB F6                           jmp 0x14047dee5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsChargeProcessQuota(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 == (*(unsigned __int64 *)(v_rip + 11832293))) goto loc_0047DEEB;
    result = PspChargeQuota(*(unsigned __int64 *)(a1 + 760), a1, 3, a3);
loc_0047DEE5:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0047DEEB:
    result = 0;
    goto loc_0047DEE5;
}
```

## 5. (Beta) C Style

```c
int64_t PsChargeProcessQuota(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == (*(uint64_t *)(v_rip + 0xB48BE5))) goto loc_0047DEEB;
    result = PspChargeQuota(*(uint64_t *)(Arg1 + 0x2F8), Arg1, 3, Arg3);
loc_0047DEE5:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0047DEEB:
    result = 0;
    goto loc_0047DEE5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047DEC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047DEC0[BB_0047DEC0]
  bb_0047DED0[BB_0047DED0]
  bb_0047DEE5[BB_0047DEE5]
  bb_0047DEEA[BB_0047DEEA]
  bb_0047DEEB[BB_0047DEEB]
  bb_0047DEC0 -->|branch| bb_0047DEEB
  bb_0047DEC0 -->|fallthrough| bb_0047DED0
  bb_0047DED0 -->|flow| bb_0047DEE5
  bb_0047DEEA -->|flow| bb_0047DEEB
  bb_0047DEEB -->|branch| bb_0047DEE5
```
