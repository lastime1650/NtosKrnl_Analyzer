# CmpVolumeContextLockShared

- RVA: `0x0087BE04`–`0x0087BE55` (길이 `81` bytes)
- VA: `0x000000014087BE04`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `26`개 명령, `81/81` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0087BE1A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0087BE3B` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [CmpVolumeContextSendDeviceUsageNotification](../7E/CmpVolumeContextSendDeviceUsageNotification_function_007E87DC.md) at `0x007E8841`
- [CmpVolumeContextCanHiveSectionBeExtended](CmpVolumeContextCanHiveSectionBeExtended_function_0087BD78.md) at `0x0087BD85`
- [CmpVolumeContextMustHiveFilePagesBeKeptLocal](CmpVolumeContextMustHiveFilePagesBeKeptLocal_function_0087BDC4.md) at `0x0087BDD1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0087BE1A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0087BE3B` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0087BE04  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0087BE09  57                              push rdi
0087BE0A  48 83 EC 20                     sub rsp, 0x20
0087BE0E  48 8D 79 38                     lea rdi, [rcx + 0x38]
0087BE12  45 33 C0                        xor r8d, r8d
0087BE15  48 8B CF                        mov rcx, rdi
0087BE18  33 D2                           xor edx, edx
0087BE1A  E8 11 44 99 FF                  call 0x140210230
0087BE1F  48 8B D8                        mov rbx, rax
0087BE22  B9 11 00 00 00                  mov ecx, 0x11
0087BE27  33 C0                           xor eax, eax
0087BE29  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0087BE2E  74 10                           je 0x14087be40
0087BE30  4C 8B CF                        mov r9, rdi
0087BE33  4C 8B C3                        mov r8, rbx
0087BE36  33 D2                           xor edx, edx
0087BE38  48 8B CF                        mov rcx, rdi
0087BE3B  E8 0C 46 99 FF                  call 0x14021044c
0087BE40  48 85 DB                        test rbx, rbx
0087BE43  74 04                           je 0x14087be49
0087BE45  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0087BE49  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0087BE4E  48 83 C4 20                     add rsp, 0x20
0087BE52  5F                              pop rdi
0087BE53  C3                              ret
0087BE54  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpVolumeContextLockShared(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 56, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 + 56;
        a3 = 0;
        a2 = 0;
        a1 = a1 + 56;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpVolumeContextLockShared(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 56, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg1 + 56;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 + 56;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0087BE04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0087BE04[BB_0087BE04]
  bb_0087BE30[BB_0087BE30]
  bb_0087BE40[BB_0087BE40]
  bb_0087BE45[BB_0087BE45]
  bb_0087BE49[BB_0087BE49]
  bb_0087BE54[BB_0087BE54]
  bb_0087BE04 -->|branch| bb_0087BE40
  bb_0087BE04 -->|fallthrough| bb_0087BE30
  bb_0087BE30 -->|flow| bb_0087BE40
  bb_0087BE40 -->|branch| bb_0087BE49
  bb_0087BE40 -->|fallthrough| bb_0087BE45
  bb_0087BE45 -->|flow| bb_0087BE49
```
