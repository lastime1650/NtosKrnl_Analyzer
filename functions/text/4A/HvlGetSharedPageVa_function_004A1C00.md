# HvlGetSharedPageVa

- RVA: `0x004A1C00`–`0x004A1C24` (길이 `36` bytes)
- VA: `0x00000001404A1C00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C74`
- 디코드: `10`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004A1C1D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [RtlGetMultiTimePrecise](RtlGetMultiTimePrecise_function_004A1A30.md) at `0x004A1A6F`
- [MiInitializeSharedUserData](../../init/C5/MiInitializeSharedUserData_function_00C5F098.md) at `0x00C5F0C3`

### Static image references
- `0x004A1C04` → RVA `0x00FC6D88` (`ALMOSTRO`; read)
- `0x004A1C16` → RVA `0x00E00C60` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A1C00  48 83 EC 28                     sub rsp, 0x28
004A1C04  48 8B 05 7D 51 B2 00            mov rax, qword ptr [rip + 0xb2517d]
004A1C0B  48 85 C0                        test rax, rax
004A1C0E  74 06                           je 0x1404a1c16
004A1C10  48 83 C4 28                     add rsp, 0x28
004A1C14  C3                              ret
004A1C15  CC                              int3
004A1C16  48 8B 05 43 F0 95 00            mov rax, qword ptr [rip + 0x95f043]
004A1C1D  E8 AE 8E 21 00                  call 0x1406baad0
004A1C22  EB EC                           jmp 0x1404a1c10
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlGetSharedPageVa(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 11686269) == 0) goto loc_004A1C16;
loc_004A1C10:
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int64 *)(v_rip + 11686269);
loc_004A1C16:
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_004A1C10;
}
```

## 5. (Beta) C Style

```c
void HvlGetSharedPageVa(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0xB2517D) == 0) goto loc_004A1C16;
loc_004A1C10:
    local_rsp = (local_rsp) + (40);
    return *(uint64_t *)(v_rip + 0xB2517D);
loc_004A1C16:
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_004A1C10;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A1C00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A1C00[BB_004A1C00]
  bb_004A1C10[BB_004A1C10]
  bb_004A1C15[BB_004A1C15]
  bb_004A1C16[BB_004A1C16]
  bb_004A1C00 -->|branch| bb_004A1C16
  bb_004A1C00 -->|fallthrough| bb_004A1C10
  bb_004A1C15 -->|flow| bb_004A1C16
  bb_004A1C16 -->|branch| bb_004A1C10
```
