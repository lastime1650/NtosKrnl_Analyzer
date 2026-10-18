# PsGetSiloBySessionId

- RVA: `0x00912F94`–`0x00912FDE` (길이 `74` bytes)
- VA: `0x0000000140912F94`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF28`
- 디코드: `21`개 명령, `74/74` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00912FA1` → [PsGetSessionById](../../text/22/PsGetSessionById_function_00225150.md) (function, `0x00225150`)
- `0x00912FC1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [SessionIsInteractive](../../text/22/SessionIsInteractive_function_0022F768.md) at `0x0022F785`
- [EtwWmitraceWorker](../7B/EtwWmitraceWorker_function_007BBD3C.md) at `0x007BBD99`
- [SeQueryServerSiloToken](SeQueryServerSiloToken_function_00912F30.md) at `0x00912F77`
- [PsIsServiceSession](PsIsServiceSession_function_00912FE4.md) at `0x00913004`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00912FA1` → [PsGetSessionById](../../text/22/PsGetSessionById_function_00225150.md) (`PAGE` → `.text`)
  - `0x00912FC1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00912F94  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00912F99  57                              push rdi
00912F9A  48 83 EC 20                     sub rsp, 0x20
00912F9E  48 8B FA                        mov rdi, rdx
00912FA1  E8 AA 21 91 FF                  call 0x140225150
00912FA6  48 8B C8                        mov rcx, rax
00912FA9  48 85 C0                        test rax, rax
00912FAC  74 29                           je 0x140912fd7
00912FAE  48 8B 80 E8 02 00 00            mov rax, qword ptr [rax + 0x2e8]
00912FB5  BA 50 73 51 79                  mov edx, 0x79517350
00912FBA  48 8B 98 A0 00 00 00            mov rbx, qword ptr [rax + 0xa0]
00912FC1  E8 1A 49 9E FF                  call 0x1402f78e0
00912FC6  33 C0                           xor eax, eax
00912FC8  48 89 1F                        mov qword ptr [rdi], rbx
00912FCB  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00912FD0  48 83 C4 20                     add rsp, 0x20
00912FD4  5F                              pop rdi
00912FD5  C3                              ret
00912FD6  CC                              int3
00912FD7  B8 55 04 00 C0                  mov eax, 0xc0000455
00912FDC  EB ED                           jmp 0x140912fcb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetSiloBySessionId(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = PsGetSessionById(a1, a2, a3, a4);
    if (result == 0) goto loc_00912FD7;
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x79517350ULL), a3, a4);
    result = 0;
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 744) + 160);
loc_00912FCB:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00912FD7:
    goto loc_00912FCB;
}
```

## 5. (Beta) C Style

```c
int64_t PsGetSiloBySessionId(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = PsGetSessionById(Arg1, Arg2, a3, a4);
    if (result == 0) goto loc_00912FD7;
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x79517350ULL), a3, a4);
    result = 0;
    *(uint64_t *)(arg2) = *(uint64_t *)(*(uint64_t *)(result + 0x2E8) + 0xA0);
loc_00912FCB:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00912FD7:
    goto loc_00912FCB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00912F94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00912F94[BB_00912F94]
  bb_00912FAE[BB_00912FAE]
  bb_00912FCB[BB_00912FCB]
  bb_00912FD6[BB_00912FD6]
  bb_00912FD7[BB_00912FD7]
  bb_00912F94 -->|branch| bb_00912FD7
  bb_00912F94 -->|fallthrough| bb_00912FAE
  bb_00912FAE -->|flow| bb_00912FCB
  bb_00912FD6 -->|flow| bb_00912FD7
  bb_00912FD7 -->|branch| bb_00912FCB
```
