# PopFxEndDeviceIRPhaseAccounting

- RVA: `0x004C9AB0`–`0x004C9AF5` (길이 `69` bytes)
- VA: `0x00000001404C9AB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064CA8`
- 디코드: `18`개 명령, `69/69` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x004C9AC0` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x004C9ADF` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x004C9AEE` → [PopFxAccumulateDeviceIRPhaseAccounting](../4B/PopFxAccumulateDeviceIRPhaseAccounting_function_004BD2CC.md) (function, `0x004BD2CC`)

### Direct callers
- [PopPdcIdleResiliencyCallback](../../page/A3/PopPdcIdleResiliencyCallback_function_00A31518.md) at `0x00A315B9`

### Static image references
- `0x004C9AB9` → RVA `0x00F0CA58` (`.data`; read)
- `0x004C9AC5` → RVA `0x00F0C7B0` (`.data`; read)
- `0x004C9AD1` → RVA `0x00F0C7B8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C9AB0  40 53                           push rbx
004C9AB2  48 83 EC 20                     sub rsp, 0x20
004C9AB6  48 8B D9                        mov rbx, rcx
004C9AB9  48 8D 0D 98 2F A4 00            lea rcx, [rip + 0xa42f98]
004C9AC0  E8 AB E9 D3 FF                  call 0x140208470
004C9AC5  48 83 3D E3 2C A4 00 00         cmp qword ptr [rip + 0xa42ce3], 0
004C9ACD  75 1C                           jne 0x1404c9aeb
004C9ACF  8A D0                           mov dl, al
004C9AD1  C6 05 E0 2C A4 00 00            mov byte ptr [rip + 0xa42ce0], 0
004C9AD8  48 8D 0D 79 2F A4 00            lea rcx, [rip + 0xa42f79]
004C9ADF  E8 BC 90 EC FF                  call 0x140392ba0
004C9AE4  48 83 C4 20                     add rsp, 0x20
004C9AE8  5B                              pop rbx
004C9AE9  C3                              ret
004C9AEA  CC                              int3
004C9AEB  48 8B CB                        mov rcx, rbx
004C9AEE  E8 D9 37 FF FF                  call 0x1404bd2cc
004C9AF3  EB DA                           jmp 0x1404c9acf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxEndDeviceIRPhaseAccounting(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 10760088, a2, a3, a4);
    if ((*(unsigned __int64 *)(v_rip + 10759395)) != 0) goto loc_004C9AEB;
loc_004C9ACF:
    *(unsigned __int8 *)(v_rip + 10759392) = 0;
    result = KeReleaseSpinLock(v_rip + 10760057, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_004C9AEB:
    result = PopFxAccumulateDeviceIRPhaseAccounting(a1, (unsigned __int8)(result), a3, a4);
    goto loc_004C9ACF;
}
```

## 5. (Beta) C Style

```c
int64_t PopFxEndDeviceIRPhaseAccounting(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 10760088, a2, a3, a4);
    if ((*(uint64_t *)(v_rip + 0xA42CE3)) != 0) goto loc_004C9AEB;
loc_004C9ACF:
    *(uint8_t *)(v_rip + 0xA42CE0) = 0;
    result = KeReleaseSpinLock(v_rip + 10760057, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_004C9AEB:
    result = PopFxAccumulateDeviceIRPhaseAccounting(Arg1, (uint8_t)(result), a3, a4);
    goto loc_004C9ACF;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C9AB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C9AB0[BB_004C9AB0]
  bb_004C9ACF[BB_004C9ACF]
  bb_004C9AEA[BB_004C9AEA]
  bb_004C9AEB[BB_004C9AEB]
  bb_004C9AB0 -->|branch| bb_004C9AEB
  bb_004C9AB0 -->|fallthrough| bb_004C9ACF
  bb_004C9AEA -->|flow| bb_004C9AEB
  bb_004C9AEB -->|branch| bb_004C9ACF
```
