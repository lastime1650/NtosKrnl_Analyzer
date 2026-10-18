# RtlpExceptionHandler

- RVA: `0x006BAF70`–`0x006BAF90` (길이 `32` bytes)
- VA: `0x00000001406BAF70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C25A8`
- 디코드: `8`개 명령, `32/32` bytes 표시
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
006BAF70  B8 01 00 00 00                  mov eax, 1
006BAF75  F7 41 04 66 00 00 00            test dword ptr [rcx + 4], 0x66
006BAF7C  75 11                           jne 0x1406baf8f
006BAF7E  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
006BAF82  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
006BAF86  49 89 41 18                     mov qword ptr [r9 + 0x18], rax
006BAF8A  B8 02 00 00 00                  mov eax, 2
006BAF8F  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpExceptionHandler(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;

    result = 1;
    if (((*(unsigned int *)(a1 + 4)) & (102)) == 0) {
        result = *(unsigned __int64 *)(a2 + 32);
        result = *(unsigned __int64 *)(result + 24);
        *(unsigned __int64 *)(a4 + 24) = result;
        result = 2;
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpExceptionHandler(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;

    result = 1;
    if (((*(uint32_t *)(arg1 + 0x4)) & (102)) == 0) {
        result = *(uint64_t *)(arg2 + 0x20);
        result = *(uint64_t *)(result + 0x18);
        *(uint64_t *)(arg4 + 0x18) = result;
        result = 2;
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg4` | `+ 0x18` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006BAF70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006BAF70[BB_006BAF70]
  bb_006BAF7E[BB_006BAF7E]
  bb_006BAF8F[BB_006BAF8F]
  bb_006BAF70 -->|branch| bb_006BAF8F
  bb_006BAF70 -->|fallthrough| bb_006BAF7E
  bb_006BAF7E -->|flow| bb_006BAF8F
```
