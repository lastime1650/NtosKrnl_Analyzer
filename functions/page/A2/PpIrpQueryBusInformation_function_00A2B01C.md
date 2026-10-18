# PpIrpQueryBusInformation

- RVA: `0x00A2B01C`–`0x00A2B081` (길이 `101` bytes)
- VA: `0x0000000140A2B01C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00087FC4`
- 디코드: `26`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A2B03E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A2B060` → [IopSynchronousCall](../8F/IopSynchronousCall_function_008FB018.md) (function, `0x008FB018`)

### Direct callers
- [PnpQueryBusInformation](PnpQueryBusInformation_function_00A2AF8C.md) at `0x00A2AFAC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A2B03E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A2B01C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A2B021  57                              push rdi
00A2B022  48 81 EC 80 00 00 00            sub rsp, 0x80
00A2B029  48 83 22 00                     and qword ptr [rdx], 0
00A2B02D  48 8B FA                        mov rdi, rdx
00A2B030  33 D2                           xor edx, edx
00A2B032  48 8B D9                        mov rbx, rcx
00A2B035  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00A2B03A  44 8D 42 48                     lea r8d, [rdx + 0x48]
00A2B03E  E8 FD BB C9 FF                  call 0x1406c6c40
00A2B043  45 33 C9                        xor r9d, r9d
00A2B046  66 C7 44 24 30 1B 15            mov word ptr [rsp + 0x30], 0x151b
00A2B04D  41 B8 BB 00 00 C0               mov r8d, 0xc00000bb
00A2B053  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00A2B058  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00A2B05D  48 8B CB                        mov rcx, rbx
00A2B060  E8 B3 FF EC FF                  call 0x1408fb018
00A2B065  85 C0                           test eax, eax
00A2B067  78 12                           js 0x140a2b07b
00A2B069  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00A2B071  48 81 C4 80 00 00 00            add rsp, 0x80
00A2B078  5F                              pop rdi
00A2B079  C3                              ret
00A2B07A  CC                              int3
00A2B07B  48 83 27 00                     and qword ptr [rdi], 0
00A2B07F  EB E8                           jmp 0x140a2b069
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpIrpQueryBusInformation(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (128);
    a2 = 0;
    result = memset(v_stack_m58, a2, a2 + 72, a4);
    a4 = 0;
    v_stack_m58 = 0x151BULL;
    v_stack_m68 = 0;
    result = IopSynchronousCall(a1, v_stack_m58, (unsigned int)(0xC00000BBULL), a4);
    if (sign_flag) goto loc_00A2B07B;
loc_00A2B069:
    v_rsp = (v_rsp) + (128);
    return result;
loc_00A2B07B:
    goto loc_00A2B069;
}
```

## 5. (Beta) C Style

```c
int64_t PpIrpQueryBusInformation(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (128);
    Arg2 = 0;
    result = memset(v_stack_m58, Arg2, Arg2 + 72, Arg4);
    Arg4 = 0;
    v_stack_m58 = 0x151BULL;
    v_stack_m68 = 0;
    result = IopSynchronousCall(Arg1, v_stack_m58, (uint32_t)(0xC00000BBULL), Arg4);
    if (sign_flag) goto loc_00A2B07B;
loc_00A2B069:
    local_rsp = (local_rsp) + (128);
    return result;
loc_00A2B07B:
    goto loc_00A2B069;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A2B01C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A2B01C[BB_00A2B01C]
  bb_00A2B069[BB_00A2B069]
  bb_00A2B07A[BB_00A2B07A]
  bb_00A2B07B[BB_00A2B07B]
  bb_00A2B01C -->|branch| bb_00A2B07B
  bb_00A2B01C -->|fallthrough| bb_00A2B069
  bb_00A2B07A -->|flow| bb_00A2B07B
  bb_00A2B07B -->|branch| bb_00A2B069
```
