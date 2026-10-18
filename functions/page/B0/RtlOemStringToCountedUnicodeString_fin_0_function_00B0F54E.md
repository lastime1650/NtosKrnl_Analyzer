# RtlOemStringToCountedUnicodeString$fin$0

- RVA: `0x00B0F54E`–`0x00B0F58E` (길이 `64` bytes)
- VA: `0x0000000140B0F54E`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00089918`
- 디코드: `22`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B0F576` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B0F576` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B0F54E  40 53                           push rbx
00B0F550  55                              push rbp
00B0F551  48 83 EC 38                     sub rsp, 0x38
00B0F555  48 8B EA                        mov rbp, rdx
00B0F558  0F B6 C1                        movzx eax, cl
00B0F55B  84 C9                           test cl, cl
00B0F55D  75 06                           jne 0x140b0f565
00B0F55F  83 7D 30 00                     cmp dword ptr [rbp + 0x30], 0
00B0F563  7D 21                           jge 0x140b0f586
00B0F565  80 BD 80 00 00 00 00            cmp byte ptr [rbp + 0x80], 0
00B0F56C  74 18                           je 0x140b0f586
00B0F56E  48 8B 5D 70                     mov rbx, qword ptr [rbp + 0x70]
00B0F572  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00B0F576  E8 D5 32 07 00                  call 0x140b82850
00B0F57B  48 83 63 08 00                  and qword ptr [rbx + 8], 0
00B0F580  33 C0                           xor eax, eax
00B0F582  66 89 43 02                     mov word ptr [rbx + 2], ax
00B0F586  48 83 C4 38                     add rsp, 0x38
00B0F58A  5D                              pop rbp
00B0F58B  5B                              pop rbx
00B0F58C  C3                              ret
00B0F58D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlOemStringToCountedUnicodeString_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
    if (a1 != 0) goto loc_00B0F565;
    if ((*(unsigned int *)(a2 + 48)) >= 0) goto loc_00B0F586;
loc_00B0F565:
    result = a1;
    if ((*(unsigned __int8 *)(a2 + 128)) != 0) {
        v_rbx = *(unsigned __int64 *)(a2 + 112);
        a1 = *(unsigned __int64 *)(v_rbx + 8);
        result = ExFreePool(a1, a2, a3, a4);
        result = 0;
        *(unsigned __int16 *)(v_rbx + 2) = 0;
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlOemStringToCountedUnicodeString_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
    if (Arg1 != 0) goto loc_00B0F565;
    if ((*(uint32_t *)(arg2 + 0x30)) >= 0) goto loc_00B0F586;
loc_00B0F565:
    result = Arg1;
    if ((*(uint8_t *)(arg2 + 0x80)) != 0) {
        local_rbx = *(uint64_t *)(arg2 + 0x70);
        Arg1 = *(uint64_t *)(local_rbx + 0x8);
        result = ExFreePool(Arg1, Arg2, a3, a4);
        result = 0;
        *(uint16_t *)(local_rbx + 0x2) = 0;
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x70` | `64` | `R` |
| `Arg2` | `+ 0x80` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B0F54E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B0F54E[BB_00B0F54E]
  bb_00B0F55F[BB_00B0F55F]
  bb_00B0F565[BB_00B0F565]
  bb_00B0F56E[BB_00B0F56E]
  bb_00B0F586[BB_00B0F586]
  bb_00B0F58D[BB_00B0F58D]
  bb_00B0F54E -->|branch| bb_00B0F565
  bb_00B0F54E -->|fallthrough| bb_00B0F55F
  bb_00B0F55F -->|branch| bb_00B0F586
  bb_00B0F55F -->|fallthrough| bb_00B0F565
  bb_00B0F565 -->|branch| bb_00B0F586
  bb_00B0F565 -->|fallthrough| bb_00B0F56E
  bb_00B0F56E -->|flow| bb_00B0F586
```
