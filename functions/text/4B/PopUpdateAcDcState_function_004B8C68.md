# PopUpdateAcDcState

- RVA: `0x004B8C68`–`0x004B8CD5` (길이 `109` bytes)
- VA: `0x00000001404B8C68`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB08C`
- 디코드: `29`개 명령, `109/109` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x004B8C9D` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x004B8CB1` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x004B8CBE` → [PopCurrentPowerState](../../page/A3/PopCurrentPowerState_function_00A356D8.md) (function, `0x00A356D8`)
- `0x004B8CCE` → [PopDiagTraceAcDcStateChange](../../page/76/PopDiagTraceAcDcStateChange_function_0076035C.md) (function, `0x0076035C`)

### Direct callers
- [PopBatteryApplyCompositeState](../../page/AE/PopBatteryApplyCompositeState_function_00AE0CD0.md) at `0x00AE0D24`

### Static image references
- `0x004B8C72` → RVA `0x00F0CE0C` (`.data`; read)
- `0x004B8C96` → RVA `0x00F0CA58` (`.data`; read)
- `0x004B8CA4` → RVA `0x00F0CE0C` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x004B8CBE` → [PopCurrentPowerState](../../page/A3/PopCurrentPowerState_function_00A356D8.md) (`.text` → `PAGE`)
  - `0x004B8CCE` → [PopDiagTraceAcDcStateChange](../../page/76/PopDiagTraceAcDcStateChange_function_0076035C.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B8C68  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004B8C6D  57                              push rdi
004B8C6E  48 83 EC 40                     sub rsp, 0x40
004B8C72  39 0D 94 41 A5 00               cmp dword ptr [rip + 0xa54194], ecx
004B8C78  0F 57 C0                        xorps xmm0, xmm0
004B8C7B  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
004B8C80  8B D9                           mov ebx, ecx
004B8C82  75 12                           jne 0x1404b8c96
004B8C84  40 32 FF                        xor dil, dil
004B8C87  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
004B8C8C  40 8A C7                        mov al, dil
004B8C8F  48 83 C4 40                     add rsp, 0x40
004B8C93  5F                              pop rdi
004B8C94  C3                              ret
004B8C95  CC                              int3
004B8C96  48 8D 0D BB 3D A5 00            lea rcx, [rip + 0xa53dbb]
004B8C9D  E8 CE F7 D4 FF                  call 0x140208470
004B8CA2  8A D0                           mov dl, al
004B8CA4  89 1D 62 41 A5 00               mov dword ptr [rip + 0xa54162], ebx
004B8CAA  48 8D 0D A7 3D A5 00            lea rcx, [rip + 0xa53da7]
004B8CB1  E8 EA 9E ED FF                  call 0x140392ba0
004B8CB6  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
004B8CBB  40 B7 01                        mov dil, 1
004B8CBE  E8 15 CA 57 00                  call 0x140a356d8
004B8CC3  44 8B 44 24 28                  mov r8d, dword ptr [rsp + 0x28]
004B8CC8  8B CB                           mov ecx, ebx
004B8CCA  8B 54 24 2C                     mov edx, dword ptr [rsp + 0x2c]
004B8CCE  E8 89 76 2A 00                  call 0x14076035c
004B8CD3  EB B2                           jmp 0x1404b8c87
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopUpdateAcDcState(int a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p2C;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (64);
    v_stack_m28 = v_xmm0;
    if ((*(unsigned int *)(v_rip + 10830228)) != a1) goto loc_004B8C96;
    v_rdi = 0;
loc_004B8C87:
    v_rsp = (v_rsp) + (64);
    return 0;
loc_004B8C96:
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 10829243, a2, a3, a4);
    *(unsigned int *)(v_rip + 10830178) = (unsigned int)(v_stack_p8);
    result = KeReleaseSpinLock(v_rip + 10829223, (unsigned __int8)(result), a3, a4);
    result = PopCurrentPowerState(v_stack_p20, (unsigned __int8)(result), a3, a4);
    result = PopDiagTraceAcDcStateChange((unsigned int)((unsigned int)(v_stack_p8)), (unsigned int)(v_stack_p2C), (unsigned int)(v_stack_p28), a4);
    goto loc_004B8C87;
}
```

## 5. (Beta) C Style

```c
int64_t PopUpdateAcDcState(int32_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p2C;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (64);
    v_stack_m28 = v_xmm0;
    if ((*(uint32_t *)(v_rip + 0xA54194)) != Arg1) goto loc_004B8C96;
    local_rdi = 0;
loc_004B8C87:
    local_rsp = (local_rsp) + (64);
    return 0;
loc_004B8C96:
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 10829243, a2, a3, a4);
    *(uint32_t *)(v_rip + 0xA54162) = (uint32_t)(v_stack_p8);
    result = KeReleaseSpinLock(v_rip + 10829223, (uint8_t)(result), a3, a4);
    result = PopCurrentPowerState(v_stack_p20, (uint8_t)(result), a3, a4);
    result = PopDiagTraceAcDcStateChange((uint32_t)((uint32_t)(v_stack_p8)), (uint32_t)(v_stack_p2C), (uint32_t)(v_stack_p28), a4);
    goto loc_004B8C87;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B8C68&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B8C68[BB_004B8C68]
  bb_004B8C84[BB_004B8C84]
  bb_004B8C87[BB_004B8C87]
  bb_004B8C95[BB_004B8C95]
  bb_004B8C96[BB_004B8C96]
  bb_004B8C68 -->|branch| bb_004B8C96
  bb_004B8C68 -->|fallthrough| bb_004B8C84
  bb_004B8C84 -->|flow| bb_004B8C87
  bb_004B8C95 -->|flow| bb_004B8C96
  bb_004B8C96 -->|branch| bb_004B8C87
```
