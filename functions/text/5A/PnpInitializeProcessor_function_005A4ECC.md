# PnpInitializeProcessor

- RVA: `0x005A4ECC`–`0x005A4F13` (길이 `71` bytes)
- VA: `0x00000001405A4ECC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `19`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005A4F06` → [PnpRequestDeviceAction](../47/PnpRequestDeviceAction_function_00477FF8.md) (function, `0x00477FF8`)

### Direct callers
- [KeStartDynamicProcessor](../../page/74/KeStartDynamicProcessor_function_00746730.md) at `0x007467B2`

### Static image references
- `0x005A4ED3` → RVA `0x00F8C438` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A4ECC  4C 8B DC                        mov r11, rsp
005A4ECF  48 83 EC 58                     sub rsp, 0x58
005A4ED3  48 8B 0D 5E 75 9E 00            mov rcx, qword ptr [rip + 0x9e755e]
005A4EDA  4D 8D 4B E8                     lea r9, [r11 - 0x18]
005A4EDE  33 C0                           xor eax, eax
005A4EE0  0F 57 C0                        xorps xmm0, xmm0
005A4EE3  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
005A4EE7  45 33 C0                        xor r8d, r8d
005A4EEA  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
005A4EEF  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
005A4EF3  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
005A4EF7  8D 50 06                        lea edx, [rax + 6]
005A4EFA  C7 44 24 48 01 00 00 00         mov dword ptr [rsp + 0x48], 1
005A4F02  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
005A4F06  E8 ED 30 ED FF                  call 0x140477ff8
005A4F0B  33 C0                           xor eax, eax
005A4F0D  48 83 C4 58                     add rsp, 0x58
005A4F11  C3                              ret
005A4F12  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpInitializeProcessor(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (88);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    a3 = 0;
    v_stack_m18 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 48) = 0;
    v_stack_m10 = 1;
    *(unsigned __int64 *)(v_rsp - 56) = 0;
    result = PnpRequestDeviceAction(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10384734) + 32), result + 6, a3, v_rsp - 24);
    result = 0;
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpInitializeProcessor(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (88);
    result = 0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    Arg3 = 0;
    v_stack_m18 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x30) = 0;
    v_stack_m10 = 1;
    *(uint64_t *)(local_rsp - 0x38) = 0;
    result = PnpRequestDeviceAction(*(uint64_t *)(*(uint64_t *)(v_rip + 0x9E755E) + 0x20), result + 6, Arg3, local_rsp - 24);
    result = 0;
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A4ECC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005A4ECC[BB_005A4ECC]
  bb_005A4F12[BB_005A4F12]
```
