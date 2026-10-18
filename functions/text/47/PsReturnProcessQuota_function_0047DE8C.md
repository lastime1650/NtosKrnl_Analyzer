# PsReturnProcessQuota

- RVA: `0x0047DE8C`–`0x0047DEB7` (길이 `43` bytes)
- VA: `0x000000014047DE8C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0047DEAC` → [PspReturnQuota](../39/PspReturnQuota_function_00390C40.md) (function, `0x00390C40`)

### Direct callers
- [MmAdjustWorkingSetSizeEx](MmAdjustWorkingSetSizeEx_function_0047D8D4.md) at `0x0047DA7D`
- [MmAdjustWorkingSetSizeEx](MmAdjustWorkingSetSizeEx_function_0047D8D4.md) at `0x0047DCE1`
- [MmAdjustWorkingSetSizeEx](MmAdjustWorkingSetSizeEx_function_0047D8D4.md) at `0x0047DD0F`
- [MmCleanProcessAddressSpace](../../page/A1/MmCleanProcessAddressSpace_function_00A17EC0.md) at `0x00A180A9`
- [MiCleanEmbryonicProcess](../../page/A1/MiCleanEmbryonicProcess_function_00A1816C.md) at `0x00A181CB`
- [MmCreateProcessAddressSpace](../../page/A5/MmCreateProcessAddressSpace_function_00A5EE5C.md) at `0x00A5F0AC`
- [MmDeleteProcessAddressSpace](../../page/AC/MmDeleteProcessAddressSpace_function_00AC804C.md) at `0x00AC8156`

### Static image references
- `0x0047DE90` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047DE8C  48 83 EC 28                     sub rsp, 0x28
0047DE90  48 3B 0D 19 8C B4 00            cmp rcx, qword ptr [rip + 0xb48c19]
0047DE97  48 8B D1                        mov rdx, rcx
0047DE9A  74 15                           je 0x14047deb1
0047DE9C  48 8B 89 F8 02 00 00            mov rcx, qword ptr [rcx + 0x2f8]
0047DEA3  4D 8B C8                        mov r9, r8
0047DEA6  41 B8 03 00 00 00               mov r8d, 3
0047DEAC  E8 8F 2D F1 FF                  call 0x140390c40
0047DEB1  48 83 C4 28                     add rsp, 0x28
0047DEB5  C3                              ret
0047DEB6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsReturnProcessQuota(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != (*(unsigned __int64 *)(v_rip + 11832345))) {
        a1 = *(unsigned __int64 *)(a1 + 760);
        a4 = a3;
        a3 = 3;
        result = PspReturnQuota(a1, a1, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsReturnProcessQuota(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != (*(uint64_t *)(v_rip + 0xB48C19))) {
        Arg1 = *(uint64_t *)(Arg1 + 0x2F8);
        a4 = Arg3;
        Arg3 = 3;
        result = PspReturnQuota(Arg1, Arg1, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047DE8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047DE8C[BB_0047DE8C]
  bb_0047DE9C[BB_0047DE9C]
  bb_0047DEB1[BB_0047DEB1]
  bb_0047DEB6[BB_0047DEB6]
  bb_0047DE8C -->|branch| bb_0047DEB1
  bb_0047DE8C -->|fallthrough| bb_0047DE9C
  bb_0047DE9C -->|flow| bb_0047DEB1
```
