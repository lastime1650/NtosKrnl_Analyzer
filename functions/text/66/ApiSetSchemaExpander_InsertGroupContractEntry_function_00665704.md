# ApiSetSchemaExpander_InsertGroupContractEntry

- RVA: `0x00665704`–`0x00665752` (길이 `78` bytes)
- VA: `0x0000000140665704`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `22`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00665738` → [ApiSetpInsertHashEntry](ApiSetpInsertHashEntry_function_006662DC.md) (function, `0x006662DC`)

### Direct callers
- [ApiSetCompose_ProcessV7Extension_Phase1](ApiSetCompose_ProcessV7Extension_Phase1_function_006641BC.md) at `0x0066445B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00665704  40 53                           push rbx
00665706  48 83 EC 30                     sub rsp, 0x30
0066570A  44 0F B7 91 B8 00 00 00         movzx r10d, word ptr [rcx + 0xb8]
00665712  48 8B D9                        mov rbx, rcx
00665715  4C 8B CA                        mov r9, rdx
00665718  66 45 89 10                     mov word ptr [r8], r10w
0066571C  45 0F B7 C2                     movzx r8d, r10w
00665720  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
00665725  41 8D 42 01                     lea eax, [r10 + 1]
00665729  66 89 81 B8 00 00 00            mov word ptr [rcx + 0xb8], ax
00665730  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00665734  48 8D 51 38                     lea rdx, [rcx + 0x38]
00665738  E8 9F 0B 00 00                  call 0x1406662dc
0066573D  85 C0                           test eax, eax
0066573F  78 0A                           js 0x14066574b
00665741  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00665745  66 FF 40 3C                     inc word ptr [rax + 0x3c]
00665749  33 C0                           xor eax, eax
0066574B  48 83 C4 30                     add rsp, 0x30
0066574F  5B                              pop rbx
00665750  C3                              ret
00665751  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ApiSetSchemaExpander_InsertGroupContractEntry(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    *(unsigned __int16 *)(a3) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 184));
    v_stack_m18 = 0;
    *(unsigned __int16 *)(a1 + 184) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 184) + 1);
    result = ApiSetpInsertHashEntry(*(unsigned __int64 *)(a1 + 32), *(unsigned __int64 *)(a1 + 32) + 56, (unsigned __int16)(*(unsigned __int16 *)(a1 + 184)), a2);
    if (!(sign_flag)) {
        result = *(unsigned __int64 *)(a1 + 32);
        result = 0;
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ApiSetSchemaExpander_InsertGroupContractEntry(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    *(uint16_t *)(arg3) = (uint16_t)(*(uint16_t *)(arg1 + 0xB8));
    v_stack_m18 = 0;
    *(uint16_t *)(arg1 + 0xB8) = (uint16_t)(*(uint16_t *)(arg1 + 0xB8) + 1);
    result = ApiSetpInsertHashEntry(*(uint64_t *)(arg1 + 0x20), *(uint64_t *)(arg1 + 0x20) + 56, (uint16_t)(*(uint16_t *)(arg1 + 0xB8)), Arg2);
    if (!(sign_flag)) {
        result = *(uint64_t *)(arg1 + 0x20);
        result = 0;
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `16` | `R` |
| `Arg1` | `+ 0xB8` | `16` | `W` |
| `Arg3` | `+ 0x0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00665704&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00665704[BB_00665704]
  bb_00665741[BB_00665741]
  bb_0066574B[BB_0066574B]
  bb_00665751[BB_00665751]
  bb_00665704 -->|branch| bb_0066574B
  bb_00665704 -->|fallthrough| bb_00665741
  bb_00665741 -->|flow| bb_0066574B
```
