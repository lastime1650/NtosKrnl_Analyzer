# FsRtlMdlWriteCompleteDev

- RVA: `0x00A979C0`–`0x00A979DC` (길이 `28` bytes)
- VA: `0x0000000140A979C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EDE0`
- 디코드: `11`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A979D3` → [CcMdlWriteComplete2](../../text/3C/CcMdlWriteComplete2_function_003CA36C.md) (function, `0x003CA36C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A979D3` → [CcMdlWriteComplete2](../../text/3C/CcMdlWriteComplete2_function_003CA36C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A979C0  48 83 EC 28                     sub rsp, 0x28
00A979C4  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
00A979C7  A8 10                           test al, 0x10
00A979C9  74 08                           je 0x140a979d3
00A979CB  32 C0                           xor al, al
00A979CD  48 83 C4 28                     add rsp, 0x28
00A979D1  C3                              ret
00A979D2  CC                              int3
00A979D3  E8 94 29 93 FF                  call 0x1403ca36c
00A979D8  B0 01                           mov al, 1
00A979DA  EB F1                           jmp 0x140a979cd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlMdlWriteCompleteDev(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (16)) == 0) goto loc_00A979D3;
    result = 0;
loc_00A979CD:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A979D3:
    result = CcMdlWriteComplete2(a1, a2, a3, a4);
    goto loc_00A979CD;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlMdlWriteCompleteDev(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (16)) == 0) goto loc_00A979D3;
    result = 0;
loc_00A979CD:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A979D3:
    result = CcMdlWriteComplete2(Arg1, a2, a3, a4);
    goto loc_00A979CD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x50` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A979C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A979C0[BB_00A979C0]
  bb_00A979CB[BB_00A979CB]
  bb_00A979CD[BB_00A979CD]
  bb_00A979D2[BB_00A979D2]
  bb_00A979D3[BB_00A979D3]
  bb_00A979C0 -->|branch| bb_00A979D3
  bb_00A979C0 -->|fallthrough| bb_00A979CB
  bb_00A979CB -->|flow| bb_00A979CD
  bb_00A979D2 -->|flow| bb_00A979D3
  bb_00A979D3 -->|branch| bb_00A979CD
```
