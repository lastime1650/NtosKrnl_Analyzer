# CmInitServerSiloState

- RVA: `0x007E5B14`–`0x007E5B8E` (길이 `122` bytes)
- VA: `0x00000001407E5B14`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000697A4`
- 디코드: `35`개 명령, `122/122` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007E5B36` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x007E5B43` → [CmpGetOrCreateContextForSiloNoRef](../9E/CmpGetOrCreateContextForSiloNoRef_function_009E7E44.md) (function, `0x009E7E44`)
- `0x007E5B57` → [CmpStartSiloRegistryNamespace](../9E/CmpStartSiloRegistryNamespace_function_009E85D0.md) (function, `0x009E85D0`)
- `0x007E5B66` → [CmpLockSiloKeyLockTrackerExclusive](../8F/CmpLockSiloKeyLockTrackerExclusive_function_008F9EF8.md) (function, `0x008F9EF8`)
- `0x007E5B72` → [CmpUnlockSiloKeyLockTracker](../9E/CmpUnlockSiloKeyLockTracker_function_009E8050.md) (function, `0x009E8050`)
- `0x007E5B7F` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)

### Direct callers
- [PspInitializeServerSiloDeferred](../77/PspInitializeServerSiloDeferred_function_0077FEE0.md) at `0x00780076`
- [CmpInitSiloSupport](CmpInitSiloSupport_function_007E5B94.md) at `0x007E5BB0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007E5B36` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x007E5B7F` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E5B14  40 53                           push rbx
007E5B16  48 83 EC 40                     sub rsp, 0x40
007E5B1A  33 C0                           xor eax, eax
007E5B1C  0F 57 C0                        xorps xmm0, xmm0
007E5B1F  48 21 44 24 58                  and qword ptr [rsp + 0x58], rax
007E5B24  4C 8B C9                        mov r9, rcx
007E5B27  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007E5B2C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007E5B31  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
007E5B36  E8 35 63 C1 FF                  call 0x1403fbe70
007E5B3B  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
007E5B40  49 8B C9                        mov rcx, r9
007E5B43  E8 FC 22 20 00                  call 0x1409e7e44
007E5B48  44 8B C0                        mov r8d, eax
007E5B4B  85 C0                           test eax, eax
007E5B4D  78 2B                           js 0x1407e5b7a
007E5B4F  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
007E5B54  48 8B CB                        mov rcx, rbx
007E5B57  E8 74 2A 20 00                  call 0x1409e85d0
007E5B5C  44 8B C0                        mov r8d, eax
007E5B5F  85 C0                           test eax, eax
007E5B61  78 17                           js 0x1407e5b7a
007E5B63  48 8B CB                        mov rcx, rbx
007E5B66  E8 8D 43 11 00                  call 0x1408f9ef8
007E5B6B  83 4B 08 01                     or dword ptr [rbx + 8], 1
007E5B6F  48 8B CB                        mov rcx, rbx
007E5B72  E8 D9 24 20 00                  call 0x1409e8050
007E5B77  45 33 C0                        xor r8d, r8d
007E5B7A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007E5B7F  E8 CC A1 C3 FF                  call 0x14041fd50
007E5B84  41 8B C0                        mov eax, r8d
007E5B87  48 83 C4 40                     add rsp, 0x40
007E5B8B  5B                              pop rbx
007E5B8C  C3                              ret
007E5B8D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmInitServerSiloState(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m28 = v_xmm0;
    result = CmpInitializeThreadInfo(v_stack_m28, a2, a3, a1);
    result = CmpGetOrCreateContextForSiloNoRef(a1, v_stack_p10, a3, a1);
    if (sign_flag) goto loc_007E5B7A;
    result = CmpStartSiloRegistryNamespace(v_stack_p10, v_stack_p10, (unsigned int)((unsigned int)(result)), a1);
    if (!(sign_flag)) {
        a1 = v_stack_p10;
        result = CmpLockSiloKeyLockTrackerExclusive(a1, v_stack_p10, (unsigned int)((unsigned int)(result)), a1);
        a1 = v_stack_p10;
        result = CmpUnlockSiloKeyLockTracker(a1, v_stack_p10, (unsigned int)((unsigned int)(result)), a1);
        a3 = 0;
    }
    result = CmCleanupThreadInfo(v_stack_m28, v_stack_p10, a3, a1);
    v_rsp = (v_rsp) + (64);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t CmInitServerSiloState(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m28 = v_xmm0;
    result = CmpInitializeThreadInfo(v_stack_m28, a2, a3, Arg1);
    result = CmpGetOrCreateContextForSiloNoRef(Arg1, v_stack_p10, a3, Arg1);
    if (sign_flag) goto loc_007E5B7A;
    result = CmpStartSiloRegistryNamespace(v_stack_p10, v_stack_p10, (uint32_t)((uint32_t)(result)), Arg1);
    if (!(sign_flag)) {
        Arg1 = v_stack_p10;
        result = CmpLockSiloKeyLockTrackerExclusive(Arg1, v_stack_p10, (uint32_t)((uint32_t)(result)), Arg1);
        Arg1 = v_stack_p10;
        result = CmpUnlockSiloKeyLockTracker(Arg1, v_stack_p10, (uint32_t)((uint32_t)(result)), Arg1);
        a3 = 0;
    }
    result = CmCleanupThreadInfo(v_stack_m28, v_stack_p10, a3, Arg1);
    local_rsp = (local_rsp) + (64);
    return 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E5B14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E5B14[BB_007E5B14]
  bb_007E5B4F[BB_007E5B4F]
  bb_007E5B63[BB_007E5B63]
  bb_007E5B7A[BB_007E5B7A]
  bb_007E5B8D[BB_007E5B8D]
  bb_007E5B14 -->|branch| bb_007E5B7A
  bb_007E5B14 -->|fallthrough| bb_007E5B4F
  bb_007E5B4F -->|branch| bb_007E5B7A
  bb_007E5B4F -->|fallthrough| bb_007E5B63
  bb_007E5B63 -->|flow| bb_007E5B7A
```
