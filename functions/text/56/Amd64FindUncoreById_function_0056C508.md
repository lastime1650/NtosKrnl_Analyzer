# Amd64FindUncoreById

- RVA: `0x0056C508`–`0x0056C51E` (길이 `22` bytes)
- VA: `0x000000014056C508`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [Amd64InitializeUncoreStatusEnhanced](Amd64InitializeUncoreStatusEnhanced_function_0056D178.md) at `0x0056D195`
- [Amd64InitializeUncoreStatusOriginal](Amd64InitializeUncoreStatusOriginal_function_0056D214.md) at `0x0056D231`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056C508  48 8B 01                        mov rax, qword ptr [rcx]
0056C50B  48 3B C1                        cmp rax, rcx
0056C50E  74 0A                           je 0x14056c51a
0056C510  39 50 14                        cmp dword ptr [rax + 0x14], edx
0056C513  74 07                           je 0x14056c51c
0056C515  48 8B 00                        mov rax, qword ptr [rax]
0056C518  EB F1                           jmp 0x14056c50b
0056C51A  33 C0                           xor eax, eax
0056C51C  C3                              ret
0056C51D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Amd64FindUncoreById(__int64 a1, int a2)
{
    __int64 result;

loc_0056C50B:
    if ((*(unsigned __int64 *)(a1)) == a1) goto loc_0056C51A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 20)) == a2) goto loc_0056C51C;
    goto loc_0056C50B;
loc_0056C51A:
    result = 0;
loc_0056C51C:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Amd64FindUncoreById(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

loc_0056C50B:
    if ((*(uint64_t *)(arg1)) == Arg1) goto loc_0056C51A;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x14)) == Arg2) goto loc_0056C51C;
    goto loc_0056C50B;
loc_0056C51A:
    result = 0;
loc_0056C51C:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056C508&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0056C508[BB_0056C508]
  bb_0056C50B[BB_0056C50B]
  bb_0056C510[BB_0056C510]
  bb_0056C515[BB_0056C515]
  bb_0056C51A[BB_0056C51A]
  bb_0056C51C[BB_0056C51C]
  bb_0056C51D[BB_0056C51D]
  bb_0056C508 -->|flow| bb_0056C50B
  bb_0056C50B -->|branch| bb_0056C51A
  bb_0056C50B -->|fallthrough| bb_0056C510
  bb_0056C510 -->|branch| bb_0056C51C
  bb_0056C510 -->|fallthrough| bb_0056C515
  bb_0056C515 -->|branch| bb_0056C50B
  bb_0056C51A -->|flow| bb_0056C51C
```
