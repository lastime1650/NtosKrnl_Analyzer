# RtlDuplicateUnicodeString$fin$0

- RVA: `0x00B0FB00`–`0x00B0FB26` (길이 `38` bytes)
- VA: `0x0000000140B0FB00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008EE24`
- 디코드: `15`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B0FB19` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B0FB19` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B0FB00  40 55                           push rbp
00B0FB02  48 83 EC 20                     sub rsp, 0x20
00B0FB06  48 8B EA                        mov rbp, rdx
00B0FB09  0F B6 C1                        movzx eax, cl
00B0FB0C  84 C9                           test cl, cl
00B0FB0E  74 0F                           je 0x140b0fb1f
00B0FB10  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00B0FB14  48 85 C9                        test rcx, rcx
00B0FB17  74 06                           je 0x140b0fb1f
00B0FB19  E8 32 2D 07 00                  call 0x140b82850
00B0FB1E  90                              nop
00B0FB1F  48 83 C4 20                     add rsp, 0x20
00B0FB23  5D                              pop rbp
00B0FB24  C3                              ret
00B0FB25  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlDuplicateUnicodeString_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (a1 == 0) goto loc_00B0FB1F;
    result = a1;
    if (*(unsigned __int64 *)(a2 + 40) != 0) {
        result = ExFreePool(*(unsigned __int64 *)(a2 + 40), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlDuplicateUnicodeString_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (Arg1 == 0) goto loc_00B0FB1F;
    result = Arg1;
    if (*(uint64_t *)(arg2 + 0x28) != 0) {
        result = ExFreePool(*(uint64_t *)(arg2 + 0x28), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B0FB00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B0FB00[BB_00B0FB00]
  bb_00B0FB10[BB_00B0FB10]
  bb_00B0FB19[BB_00B0FB19]
  bb_00B0FB1F[BB_00B0FB1F]
  bb_00B0FB25[BB_00B0FB25]
  bb_00B0FB00 -->|branch| bb_00B0FB1F
  bb_00B0FB00 -->|fallthrough| bb_00B0FB10
  bb_00B0FB10 -->|branch| bb_00B0FB1F
  bb_00B0FB10 -->|fallthrough| bb_00B0FB19
  bb_00B0FB19 -->|flow| bb_00B0FB1F
```
