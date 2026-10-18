# PsGetProcessWow64Process

- RVA: `0x0041DAC0`–`0x0041DAD3` (길이 `19` bytes)
- VA: `0x000000014041DAC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `19/19` bytes 표시
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
0041DAC0  48 8B 81 10 03 00 00            mov rax, qword ptr [rcx + 0x310]
0041DAC7  48 85 C0                        test rax, rax
0041DACA  74 05                           je 0x14041dad1
0041DACC  48 8B 00                        mov rax, qword ptr [rax]
0041DACF  C3                              ret
0041DAD0  CC                              int3
0041DAD1  C3                              ret
0041DAD2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetProcessWow64Process(__int64 a1)
{
    if (*(unsigned __int64 *)(a1 + 784) == 0) goto loc_0041DAD1;
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 784));
loc_0041DAD1:
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 784));
}
```

## 5. (Beta) C Style

```c
int64_t PsGetProcessWow64Process(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (*(uint64_t *)(arg1 + 0x310) == 0) goto loc_0041DAD1;
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0x310));
loc_0041DAD1:
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0x310));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x310` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041DAC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041DAC0[BB_0041DAC0]
  bb_0041DACC[BB_0041DACC]
  bb_0041DAD0[BB_0041DAD0]
  bb_0041DAD1[BB_0041DAD1]
  bb_0041DAD2[BB_0041DAD2]
  bb_0041DAC0 -->|branch| bb_0041DAD1
  bb_0041DAC0 -->|fallthrough| bb_0041DACC
  bb_0041DAD0 -->|flow| bb_0041DAD1
```
