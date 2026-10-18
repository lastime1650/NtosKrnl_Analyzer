# RtlUpcaseUnicodeStringToCountedOemString$fin$0

- RVA: `0x00B0F4BC`–`0x00B0F4FF` (길이 `67` bytes)
- VA: `0x0000000140B0F4BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00089780`
- 디코드: `22`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B0F4E7` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B0F4E7` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B0F4BC  40 53                           push rbx
00B0F4BE  55                              push rbp
00B0F4BF  48 83 EC 48                     sub rsp, 0x48
00B0F4C3  48 8B EA                        mov rbp, rdx
00B0F4C6  0F B6 C1                        movzx eax, cl
00B0F4C9  84 C9                           test cl, cl
00B0F4CB  75 06                           jne 0x140b0f4d3
00B0F4CD  83 7D 40 00                     cmp dword ptr [rbp + 0x40], 0
00B0F4D1  7D 24                           jge 0x140b0f4f7
00B0F4D3  80 BD A0 00 00 00 00            cmp byte ptr [rbp + 0xa0], 0
00B0F4DA  74 1B                           je 0x140b0f4f7
00B0F4DC  48 8B 9D 90 00 00 00            mov rbx, qword ptr [rbp + 0x90]
00B0F4E3  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00B0F4E7  E8 64 33 07 00                  call 0x140b82850
00B0F4EC  48 83 63 08 00                  and qword ptr [rbx + 8], 0
00B0F4F1  33 C0                           xor eax, eax
00B0F4F3  66 89 43 02                     mov word ptr [rbx + 2], ax
00B0F4F7  48 83 C4 48                     add rsp, 0x48
00B0F4FB  5D                              pop rbp
00B0F4FC  5B                              pop rbx
00B0F4FD  C3                              ret
00B0F4FE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlUpcaseUnicodeStringToCountedOemString_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (72);
    if (a1 != 0) goto loc_00B0F4D3;
    if ((*(unsigned int *)(a2 + 64)) >= 0) goto loc_00B0F4F7;
loc_00B0F4D3:
    result = a1;
    if ((*(unsigned __int8 *)(a2 + 160)) != 0) {
        v_rbx = *(unsigned __int64 *)(a2 + 144);
        a1 = *(unsigned __int64 *)(v_rbx + 8);
        result = ExFreePool(a1, a2, a3, a4);
        result = 0;
        *(unsigned __int16 *)(v_rbx + 2) = 0;
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlUpcaseUnicodeStringToCountedOemString_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (72);
    if (Arg1 != 0) goto loc_00B0F4D3;
    if ((*(uint32_t *)(arg2 + 0x40)) >= 0) goto loc_00B0F4F7;
loc_00B0F4D3:
    result = Arg1;
    if ((*(uint8_t *)(arg2 + 0xA0)) != 0) {
        local_rbx = *(uint64_t *)(arg2 + 0x90);
        Arg1 = *(uint64_t *)(local_rbx + 0x8);
        result = ExFreePool(Arg1, Arg2, a3, a4);
        result = 0;
        *(uint16_t *)(local_rbx + 0x2) = 0;
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `32` | `R` |
| `Arg2` | `+ 0x90` | `64` | `R` |
| `Arg2` | `+ 0xA0` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B0F4BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B0F4BC[BB_00B0F4BC]
  bb_00B0F4CD[BB_00B0F4CD]
  bb_00B0F4D3[BB_00B0F4D3]
  bb_00B0F4DC[BB_00B0F4DC]
  bb_00B0F4F7[BB_00B0F4F7]
  bb_00B0F4FE[BB_00B0F4FE]
  bb_00B0F4BC -->|branch| bb_00B0F4D3
  bb_00B0F4BC -->|fallthrough| bb_00B0F4CD
  bb_00B0F4CD -->|branch| bb_00B0F4F7
  bb_00B0F4CD -->|fallthrough| bb_00B0F4D3
  bb_00B0F4D3 -->|branch| bb_00B0F4F7
  bb_00B0F4D3 -->|fallthrough| bb_00B0F4DC
  bb_00B0F4DC -->|flow| bb_00B0F4F7
```
