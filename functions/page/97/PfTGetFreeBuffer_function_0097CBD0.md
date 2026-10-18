# PfTGetFreeBuffer

- RVA: `0x0097CBD0`–`0x0097CBF0` (길이 `32` bytes)
- VA: `0x000000014097CBD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PfTAllocateBuffers](../75/PfTAllocateBuffers_function_0075110C.md) at `0x007511BA`
- [PfTReplaceCurrentBuffer](PfTReplaceCurrentBuffer_function_0097CB14.md) at `0x0097CB23`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0097CBD0  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
0097CBD4  33 C0                           xor eax, eax
0097CBD6  48 85 D2                        test rdx, rdx
0097CBD9  74 13                           je 0x14097cbee
0097CBDB  48 8B 02                        mov rax, qword ptr [rdx]
0097CBDE  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
0097CBE2  48 8B C2                        mov rax, rdx
0097CBE5  BA FF FF 00 00                  mov edx, 0xffff
0097CBEA  66 01 51 0A                     add word ptr [rcx + 0xa], dx
0097CBEE  C3                              ret
0097CBEF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfTGetFreeBuffer(__int64 a1)
{
    __int64 result;

    result = 0;
    if (*(unsigned __int64 *)(a1 + 16) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16));
        *(unsigned __int64 *)(a1 + 16) = result;
        result = *(unsigned __int64 *)(a1 + 16);
        a2 = 0xFFFFULL;
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfTGetFreeBuffer(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = 0;
    if (*(uint64_t *)(arg1 + 0x10) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10));
        *(uint64_t *)(arg1 + 0x10) = result;
        result = *(uint64_t *)(arg1 + 0x10);
        a2 = 0xFFFFULL;
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xA` | `16` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097CBD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0097CBD0[BB_0097CBD0]
  bb_0097CBDB[BB_0097CBDB]
  bb_0097CBEE[BB_0097CBEE]
  bb_0097CBEF[BB_0097CBEF]
  bb_0097CBD0 -->|branch| bb_0097CBEE
  bb_0097CBD0 -->|fallthrough| bb_0097CBDB
  bb_0097CBDB -->|flow| bb_0097CBEE
```
