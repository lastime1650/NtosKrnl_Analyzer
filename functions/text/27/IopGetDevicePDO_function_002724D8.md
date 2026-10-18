# IopGetDevicePDO

- RVA: `0x002724D8`–`0x00272533` (길이 `91` bytes)
- VA: `0x00000001402724D8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065BB8`
- 디코드: `26`개 명령, `91/91` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002724EA` → [KeAcquireQueuedSpinLock](KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x002724F5` → [IopGetDeviceAttachmentBase](IopGetDeviceAttachmentBase_function_002726E0.md) (function, `0x002726E0`)
- `0x0027250E` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0027251B` → [KeReleaseQueuedSpinLock](KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)

### Direct callers
- [IoAllowExecution](IoAllowExecution_function_00272498.md) at `0x002724A2`
- [IoRevokeHandlesForProcess](../59/IoRevokeHandlesForProcess_function_005981A8.md) at `0x005982D5`
- [IoRegisterContainerNotification](../../page/71/IoRegisterContainerNotification_function_0071E700.md) at `0x0071E8F0`
- [IopGetNumaNodeInformation](../../page/72/IopGetNumaNodeInformation_function_00720F68.md) at `0x00720F89`
- [IopGetSetSecurityObject](../../page/87/IopGetSetSecurityObject_function_00873A80.md) at `0x00873FAD`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x008A022F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002724D8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002724DD  57                              push rdi
002724DE  48 83 EC 20                     sub rsp, 0x20
002724E2  48 8B D9                        mov rbx, rcx
002724E5  B9 0A 00 00 00                  mov ecx, 0xa
002724EA  E8 91 18 00 00                  call 0x140273d80
002724EF  48 8B CB                        mov rcx, rbx
002724F2  40 8A F8                        mov dil, al
002724F5  E8 E6 01 00 00                  call 0x1402726e0
002724FA  48 8B D8                        mov rbx, rax
002724FD  F7 40 30 00 10 00 00            test dword ptr [rax + 0x30], 0x1000
00272504  74 29                           je 0x14027252f
00272506  BA 44 66 6C 74                  mov edx, 0x746c6644
0027250B  48 8B C8                        mov rcx, rax
0027250E  E8 FD E1 F9 FF                  call 0x140210710
00272513  40 8A D7                        mov dl, dil
00272516  B9 0A 00 00 00                  mov ecx, 0xa
0027251B  E8 20 00 00 00                  call 0x140272540
00272520  48 8B C3                        mov rax, rbx
00272523  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00272528  48 83 C4 20                     add rsp, 0x20
0027252C  5F                              pop rdi
0027252D  C3                              ret
0027252E  CC                              int3
0027252F  33 DB                           xor ebx, ebx
00272531  EB E0                           jmp 0x140272513
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopGetDevicePDO(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = KeAcquireQueuedSpinLock(10, a2, a3, a4);
    result = IopGetDeviceAttachmentBase(a1, a2, a3, a4);
    if (((*(unsigned int *)(result + 48)) & (0x1000ULL)) == 0) goto loc_0027252F;
    result = ObfReferenceObjectWithTag(result, (unsigned int)(0x746C6644ULL), a3, a4);
loc_00272513:
    result = KeReleaseQueuedSpinLock(10, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_0027252F:
    v_rbx = 0;
    goto loc_00272513;
}
```

## 5. (Beta) C Style

```c
int64_t IopGetDevicePDO(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = KeAcquireQueuedSpinLock(10, a2, a3, a4);
    result = IopGetDeviceAttachmentBase(Arg1, a2, a3, a4);
    if (((*(uint32_t *)(result + 0x30)) & (0x1000ULL)) == 0) goto loc_0027252F;
    result = ObfReferenceObjectWithTag(result, (uint32_t)(0x746C6644ULL), a3, a4);
loc_00272513:
    result = KeReleaseQueuedSpinLock(10, (uint8_t)((uint8_t)(result)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_0027252F:
    local_rbx = 0;
    goto loc_00272513;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002724D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002724D8[BB_002724D8]
  bb_00272506[BB_00272506]
  bb_00272513[BB_00272513]
  bb_0027252E[BB_0027252E]
  bb_0027252F[BB_0027252F]
  bb_002724D8 -->|branch| bb_0027252F
  bb_002724D8 -->|fallthrough| bb_00272506
  bb_00272506 -->|flow| bb_00272513
  bb_0027252E -->|flow| bb_0027252F
  bb_0027252F -->|branch| bb_00272513
```
