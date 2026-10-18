# ViSpRtlAnsiStringToUnicodeString_Exit

- RVA: `0x00BB4DB0`–`0x00BB4DD2` (길이 `34` bytes)
- VA: `0x0000000140BB4DB0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BB4DC7` → [ViSpRtlReplaceStringBuffer](ViSpRtlReplaceStringBuffer_function_00BB4E34.md) (function, `0x00BB4E34`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB4DB0  48 83 EC 28                     sub rsp, 0x28
00BB4DB4  80 79 08 00                     cmp byte ptr [rcx + 8], 0
00BB4DB8  74 12                           je 0x140bb4dcc
00BB4DBA  83 79 20 00                     cmp dword ptr [rcx + 0x20], 0
00BB4DBE  7C 0C                           jl 0x140bb4dcc
00BB4DC0  48 8B 11                        mov rdx, qword ptr [rcx]
00BB4DC3  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00BB4DC7  E8 68 00 00 00                  call 0x140bb4e34
00BB4DCC  48 83 C4 28                     add rsp, 0x28
00BB4DD0  C3                              ret
00BB4DD1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViSpRtlAnsiStringToUnicodeString_Exit(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(a1 + 8)) == 0) goto loc_00BB4DCC;
    if ((*(unsigned int *)(a1 + 32)) >= 0) {
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 24);
        result = ViSpRtlReplaceStringBuffer(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViSpRtlAnsiStringToUnicodeString_Exit(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(arg1 + 0x8)) == 0) goto loc_00BB4DCC;
    if ((*(uint32_t *)(arg1 + 0x20)) >= 0) {
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x18);
        result = ViSpRtlReplaceStringBuffer(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB4DB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BB4DB0[BB_00BB4DB0]
  bb_00BB4DBA[BB_00BB4DBA]
  bb_00BB4DC0[BB_00BB4DC0]
  bb_00BB4DCC[BB_00BB4DCC]
  bb_00BB4DD1[BB_00BB4DD1]
  bb_00BB4DB0 -->|branch| bb_00BB4DCC
  bb_00BB4DB0 -->|fallthrough| bb_00BB4DBA
  bb_00BB4DBA -->|branch| bb_00BB4DCC
  bb_00BB4DBA -->|fallthrough| bb_00BB4DC0
  bb_00BB4DC0 -->|flow| bb_00BB4DCC
```
