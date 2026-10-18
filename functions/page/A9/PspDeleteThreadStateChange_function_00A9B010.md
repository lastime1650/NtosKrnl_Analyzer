# PspDeleteThreadStateChange

- RVA: `0x00A9B010`–`0x00A9B042` (길이 `50` bytes)
- VA: `0x0000000140A9B010`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007EE6C`
- 디코드: `17`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A9B02A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00A9B03B` → [PsMultiResumeThread](../../text/20/PsMultiResumeThread_function_002027C4.md) (function, `0x002027C4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A9B02A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00A9B03B` → [PsMultiResumeThread](../../text/20/PsMultiResumeThread_function_002027C4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A9B010  40 53                           push rbx
00A9B012  48 83 EC 20                     sub rsp, 0x20
00A9B016  44 8B 41 14                     mov r8d, dword ptr [rcx + 0x14]
00A9B01A  48 8B D9                        mov rbx, rcx
00A9B01D  45 85 C0                        test r8d, r8d
00A9B020  75 14                           jne 0x140a9b036
00A9B022  48 8B 0B                        mov rcx, qword ptr [rbx]
00A9B025  BA 50 73 54 63                  mov edx, 0x63547350
00A9B02A  E8 B1 C8 85 FF                  call 0x1402f78e0
00A9B02F  48 83 C4 20                     add rsp, 0x20
00A9B033  5B                              pop rbx
00A9B034  C3                              ret
00A9B035  CC                              int3
00A9B036  48 8B 09                        mov rcx, qword ptr [rcx]
00A9B039  33 D2                           xor edx, edx
00A9B03B  E8 84 77 76 FF                  call 0x1402027c4
00A9B040  EB E0                           jmp 0x140a9b022
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspDeleteThreadStateChange(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20))) != 0) goto loc_00A9B036;
loc_00A9B022:
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1), (unsigned int)(0x63547350ULL), (unsigned int)(*(unsigned int *)(a1 + 20)), a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A9B036:
    a2 = 0;
    result = PsMultiResumeThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)), a2, (unsigned int)(*(unsigned int *)(a1 + 20)), a4);
    goto loc_00A9B022;
}
```

## 5. (Beta) C Style

```c
int64_t PspDeleteThreadStateChange(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14))) != 0) goto loc_00A9B036;
loc_00A9B022:
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1), (uint32_t)(0x63547350ULL), (uint32_t)(*(uint32_t *)(arg1 + 0x14)), a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A9B036:
    a2 = 0;
    result = PsMultiResumeThread(*(uint64_t *)(*(uint64_t *)(arg1)), a2, (uint32_t)(*(uint32_t *)(arg1 + 0x14)), a4);
    goto loc_00A9B022;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A9B010&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A9B010[BB_00A9B010]
  bb_00A9B022[BB_00A9B022]
  bb_00A9B035[BB_00A9B035]
  bb_00A9B036[BB_00A9B036]
  bb_00A9B010 -->|branch| bb_00A9B036
  bb_00A9B010 -->|fallthrough| bb_00A9B022
  bb_00A9B035 -->|flow| bb_00A9B036
  bb_00A9B036 -->|branch| bb_00A9B022
```
