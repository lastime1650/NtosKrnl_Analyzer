# SmStoreDecompressBuffer$fin$0

- RVA: `0x006D299D`–`0x006D29C8` (길이 `43` bytes)
- VA: `0x00000001406D299D`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000899F8`
- 디코드: `14`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D29BB` → [SmStoreDecompressBufferContextCleanup](../48/SmStoreDecompressBufferContextCleanup_function_00485368.md) (function, `0x00485368`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D299D  40 55                           push rbp
006D299F  48 83 EC 40                     sub rsp, 0x40
006D29A3  48 8B EA                        mov rbp, rdx
006D29A6  0F B6 C1                        movzx eax, cl
006D29A9  84 C9                           test cl, cl
006D29AB  74 14                           je 0x1406d29c1
006D29AD  C7 85 84 00 00 00 01 00 00 C0   mov dword ptr [rbp + 0x84], 0xc0000001
006D29B7  48 8D 4D 58                     lea rcx, [rbp + 0x58]
006D29BB  E8 A8 29 DB FF                  call 0x140485368
006D29C0  90                              nop
006D29C1  48 83 C4 40                     add rsp, 0x40
006D29C5  5D                              pop rbp
006D29C6  C3                              ret
006D29C7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SmStoreDecompressBuffer_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (64);
    result = a1;
    if (a1 != 0) {
        *(unsigned int *)(a2 + 132) = 0xC0000001ULL;
        a1 = a2 + 88;
        result = SmStoreDecompressBufferContextCleanup(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SmStoreDecompressBuffer_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (64);
    result = Arg1;
    if (Arg1 != 0) {
        *(uint32_t *)(arg2 + 0x84) = 0xC0000001ULL;
        Arg1 = Arg2 + 88;
        result = SmStoreDecompressBufferContextCleanup(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x84` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D299D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D299D[BB_006D299D]
  bb_006D29AD[BB_006D29AD]
  bb_006D29C1[BB_006D29C1]
  bb_006D29C7[BB_006D29C7]
  bb_006D299D -->|branch| bb_006D29C1
  bb_006D299D -->|fallthrough| bb_006D29AD
  bb_006D29AD -->|flow| bb_006D29C1
```
