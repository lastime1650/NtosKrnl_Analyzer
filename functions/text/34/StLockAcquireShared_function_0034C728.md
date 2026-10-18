# StLockAcquireShared

- RVA: `0x0034C728`–`0x0034C78B` (길이 `99` bytes)
- VA: `0x000000014034C728`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `29`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0034C74B` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0034C76C` → [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmReadPickStore](SMKM_STORE_MGR_SM_TRAITS_SmReadPickStore_function_0034C494.md) at `0x0034C4CC`
- [sub_0034CA36](Unknown_function_0034CA36.md) at `0x0034CA3D`
- [sub_0034CAB5](Unknown_function_0034CAB5.md) at `0x0034CAF6`
- [sub_0034CCB2](Unknown_function_0034CCB2.md) at `0x0034CD04`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStMapVirtualRegion](SMKM_STORE_SM_TRAITS_SmStMapVirtualRegion_function_0034D770.md) at `0x0034D7D0`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStPrioritizeRegionsStore](SMKM_STORE_SM_TRAITS_SmStPrioritizeRegionsStore_function_0034DE28.md) at `0x0034DEC7`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStPrioritizeRegionsStore](SMKM_STORE_SM_TRAITS_SmStPrioritizeRegionsStore_function_0034DE28.md) at `0x0034E0E7`
- [sub_004201AA](../42/Unknown_function_004201AA.md) at `0x00420229`
- [sub_004201AA](../42/Unknown_function_004201AA.md) at `0x0042029C`
- [sub_004201AA](../42/Unknown_function_004201AA.md) at `0x004202B2`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStInSwapStore](../49/SMKM_STORE_SM_TRAITS_SmStInSwapStore_function_00496BC8.md) at `0x00496C4E`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStOutSwapStore](../49/SMKM_STORE_SM_TRAITS_SmStOutSwapStore_function_00496C84.md) at `0x00496D0B`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStOutSwapStore](../49/SMKM_STORE_SM_TRAITS_SmStOutSwapStore_function_00496C84.md) at `0x00496F43`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStTrimWsStore](../4B/SMKM_STORE_SM_TRAITS_SmStTrimWsStore_function_004BEB4C.md) at `0x004BEC04`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmHandleDecompressionFailure](../60/ST_STORE_SM_TRAITS_StDmHandleDecompressionFailure_function_0060DA74.md) at `0x0060DB08`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0034C728  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0034C72D  57                              push rdi
0034C72E  48 83 EC 20                     sub rsp, 0x20
0034C732  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0034C73B  45 33 C0                        xor r8d, r8d
0034C73E  33 D2                           xor edx, edx
0034C740  48 8B F9                        mov rdi, rcx
0034C743  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
0034C74A  90                              nop
0034C74B  E8 E0 3A EC FF                  call 0x140210230
0034C750  48 8B D8                        mov rbx, rax
0034C753  B9 11 00 00 00                  mov ecx, 0x11
0034C758  33 C0                           xor eax, eax
0034C75A  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0034C75F  74 10                           je 0x14034c771
0034C761  4C 8B CF                        mov r9, rdi
0034C764  4C 8B C3                        mov r8, rbx
0034C767  33 D2                           xor edx, edx
0034C769  48 8B CF                        mov rcx, rdi
0034C76C  E8 DB 3C EC FF                  call 0x14021044c
0034C771  48 85 DB                        test rbx, rbx
0034C774  74 04                           je 0x14034c77a
0034C776  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0034C77A  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0034C77F  B8 02 00 00 00                  mov eax, 2
0034C784  48 83 C4 20                     add rsp, 0x20
0034C788  5F                              pop rdi
0034C789  C3                              ret
0034C78A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall StLockAcquireShared(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1;
        a3 = 0;
        a2 = 0;
        a1 = a1;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return 2;
}
```

## 5. (Beta) C Style

```c
int64_t StLockAcquireShared(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg1;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return 2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0034C728&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0034C728[BB_0034C728]
  bb_0034C761[BB_0034C761]
  bb_0034C771[BB_0034C771]
  bb_0034C776[BB_0034C776]
  bb_0034C77A[BB_0034C77A]
  bb_0034C78A[BB_0034C78A]
  bb_0034C728 -->|branch| bb_0034C771
  bb_0034C728 -->|fallthrough| bb_0034C761
  bb_0034C761 -->|flow| bb_0034C771
  bb_0034C771 -->|branch| bb_0034C77A
  bb_0034C771 -->|fallthrough| bb_0034C776
  bb_0034C776 -->|flow| bb_0034C77A
```
