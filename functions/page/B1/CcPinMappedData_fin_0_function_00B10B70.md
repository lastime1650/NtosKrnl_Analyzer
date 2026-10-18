# CcPinMappedData$fin$0

- RVA: `0x00B10B70`–`0x00B10B9F` (길이 `47` bytes)
- VA: `0x0000000140B10B70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A1F78`
- 디코드: `16`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B10B92` → [CcUnpinData](../9A/CcUnpinData_function_009A7A80.md) (function, `0x009A7A80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B10B70  40 55                           push rbp
00B10B72  48 83 EC 50                     sub rsp, 0x50
00B10B76  48 8B EA                        mov rbp, rdx
00B10B79  80 7D 50 00                     cmp byte ptr [rbp + 0x50], 0
00B10B7D  75 19                           jne 0x140b10b98
00B10B7F  48 8B 85 D0 00 00 00            mov rax, qword ptr [rbp + 0xd0]
00B10B86  48 FF 00                        inc qword ptr [rax]
00B10B89  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00B10B8D  48 85 C9                        test rcx, rcx
00B10B90  74 06                           je 0x140b10b98
00B10B92  E8 E9 6E E9 FF                  call 0x1409a7a80
00B10B97  90                              nop
00B10B98  48 83 C4 50                     add rsp, 0x50
00B10B9C  5D                              pop rbp
00B10B9D  C3                              ret
00B10B9E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcPinMappedData_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (80);
    if ((*(unsigned __int8 *)(a2 + 80)) != 0) goto loc_00B10B98;
    result = *(unsigned __int64 *)(a2 + 208);
    if (*(unsigned __int64 *)(a2 + 88) != 0) {
        result = CcUnpinData(*(unsigned __int64 *)(a2 + 88), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcPinMappedData_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (80);
    if ((*(uint8_t *)(arg2 + 0x50)) != 0) goto loc_00B10B98;
    result = *(uint64_t *)(arg2 + 0xD0);
    if (*(uint64_t *)(arg2 + 0x58) != 0) {
        result = CcUnpinData(*(uint64_t *)(arg2 + 0x58), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x50` | `8` | `R` |
| `Arg2` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0xD0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B10B70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B10B70[BB_00B10B70]
  bb_00B10B7F[BB_00B10B7F]
  bb_00B10B92[BB_00B10B92]
  bb_00B10B98[BB_00B10B98]
  bb_00B10B9E[BB_00B10B9E]
  bb_00B10B70 -->|branch| bb_00B10B98
  bb_00B10B70 -->|fallthrough| bb_00B10B7F
  bb_00B10B7F -->|branch| bb_00B10B98
  bb_00B10B7F -->|fallthrough| bb_00B10B92
  bb_00B10B92 -->|flow| bb_00B10B98
```
