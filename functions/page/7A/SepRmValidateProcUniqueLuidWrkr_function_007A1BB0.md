# SepRmValidateProcUniqueLuidWrkr

- RVA: `0x007A1BB0`–`0x007A1BD6` (길이 `38` bytes)
- VA: `0x00000001407A1BB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007A1BC7` → [SepIsValidProcUniqueLuid](SepIsValidProcUniqueLuid_function_007A28B0.md) (function, `0x007A28B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007A1BB0  40 53                           push rbx
007A1BB2  48 83 EC 20                     sub rsp, 0x20
007A1BB6  48 8B 41 2C                     mov rax, qword ptr [rcx + 0x2c]
007A1BBA  48 8B DA                        mov rbx, rdx
007A1BBD  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
007A1BC2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007A1BC7  E8 E4 0C 00 00                  call 0x1407a28b0
007A1BCC  89 43 28                        mov dword ptr [rbx + 0x28], eax
007A1BCF  48 83 C4 20                     add rsp, 0x20
007A1BD3  5B                              pop rbx
007A1BD4  C3                              ret
007A1BD5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepRmValidateProcUniqueLuidWrkr(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (32);
    v_stack_p8 = *(unsigned __int64 *)(a1 + 44);
    result = SepIsValidProcUniqueLuid(v_stack_p8, a2, a3, a4);
    *(unsigned int *)(a2 + 40) = (unsigned int)(result);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepRmValidateProcUniqueLuidWrkr(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    v_stack_p8 = *(uint64_t *)(arg1 + 0x2C);
    result = SepIsValidProcUniqueLuid(v_stack_p8, Arg2, a3, a4);
    *(uint32_t *)(arg2 + 0x28) = (uint32_t)(result);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2C` | `64` | `R` |
| `Arg2` | `+ 0x28` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007A1BB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007A1BB0[BB_007A1BB0]
  bb_007A1BD5[BB_007A1BD5]
```
