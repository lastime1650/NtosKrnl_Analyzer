# MiCountSlabContextAvailablePagesForDefrag

- RVA: `0x0068D250`–`0x0068D271` (길이 `33` bytes)
- VA: `0x000000014068D250`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0068D250  4C 8B 4A 60                     mov r9, qword ptr [rdx + 0x60]
0068D254  48 8B 42 50                     mov rax, qword ptr [rdx + 0x50]
0068D258  48 8B 00                        mov rax, qword ptr [rax]
0068D25B  48 8B 4A 68                     mov rcx, qword ptr [rdx + 0x68]
0068D25F  49 03 C1                        add rax, r9
0068D262  48 3B C1                        cmp rax, rcx
0068D265  76 06                           jbe 0x14068d26d
0068D267  48 2B C1                        sub rax, rcx
0068D26A  49 01 00                        add qword ptr [r8], rax
0068D26D  33 C0                           xor eax, eax
0068D26F  C3                              ret
0068D270  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCountSlabContextAvailablePagesForDefrag(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 80))) + (*(unsigned __int64 *)(a2 + 96));
    if (result >= = (*(unsigned __int64 *)(a2 + 104))) {
        result = (result) - (*(unsigned __int64 *)(a2 + 104));
    }
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiCountSlabContextAvailablePagesForDefrag(int64_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    result = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x50))) + (*(uint64_t *)(arg2 + 0x60));
    if (result >= = (*(uint64_t *)(arg2 + 0x68))) {
        result = (result) - (*(uint64_t *)(arg2 + 0x68));
    }
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x50` | `64` | `R` |
| `Arg2` | `+ 0x60` | `64` | `R` |
| `Arg2` | `+ 0x68` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0068D250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0068D250[BB_0068D250]
  bb_0068D267[BB_0068D267]
  bb_0068D26D[BB_0068D26D]
  bb_0068D270[BB_0068D270]
  bb_0068D250 -->|branch| bb_0068D26D
  bb_0068D250 -->|fallthrough| bb_0068D267
  bb_0068D267 -->|flow| bb_0068D26D
```
