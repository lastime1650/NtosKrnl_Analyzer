# AuthzBasepEqualUnicodeStringCaseSensitive

- RVA: `0x003A8A44`–`0x003A8A6F` (길이 `43` bytes)
- VA: `0x00000001403A8A44`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006DBD4`
- 디코드: `15`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003A8A63` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)

### Direct callers
- [sub_00213726](../21/Unknown_function_00213726.md) at `0x0021374F`
- [AuthzBasepCompareUnicodeStringOperands](../2F/AuthzBasepCompareUnicodeStringOperands_function_002FE26C.md) at `0x002FE442`
- [sub_003001D4](../30/Unknown_function_003001D4.md) at `0x003001D4`
- [sub_003A7C9B](Unknown_function_003A7C9B.md) at `0x003A7C9B`
- [sub_003A80B2](Unknown_function_003A80B2.md) at `0x003A80B2`
- [AuthzBasepCopyoutSecurityAttributes](AuthzBasepCopyoutSecurityAttributes_function_003A8100.md) at `0x003A83C1`
- [AuthzBasepSecurityAttributePresent](AuthzBasepSecurityAttributePresent_function_003A88B0.md) at `0x003A894B`
- [AuthzBasepFindSecurityAttribute](AuthzBasepFindSecurityAttribute_function_003A8980.md) at `0x003A8A17`
- [AuthzBasepEqualUnicodeString](AuthzBasepEqualUnicodeString_function_003A8A80.md) at `0x003A8A9A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A8A44  48 83 EC 28                     sub rsp, 0x28
003A8A48  0F B7 01                        movzx eax, word ptr [rcx]
003A8A4B  66 3B 02                        cmp ax, word ptr [rdx]
003A8A4E  74 08                           je 0x1403a8a58
003A8A50  32 C0                           xor al, al
003A8A52  48 83 C4 28                     add rsp, 0x28
003A8A56  C3                              ret
003A8A57  CC                              int3
003A8A58  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
003A8A5C  4C 8B C0                        mov r8, rax
003A8A5F  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
003A8A63  E8 A8 E0 31 00                  call 0x1406c6b10
003A8A68  85 C0                           test eax, eax
003A8A6A  0F 94 C0                        sete al
003A8A6D  EB E3                           jmp 0x1403a8a52
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AuthzBasepEqualUnicodeStringCaseSensitive(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) == (*(unsigned __int16 *)(a2))) goto loc_003A8A58;
    result = 0;
loc_003A8A52:
    v_rsp = (v_rsp) + (40);
    return result;
loc_003A8A58:
    result = memcmp(*(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a2 + 8), 0, a4);
    result = ((unsigned int)(result) == 0) ? 1 : 0;
    goto loc_003A8A52;
}
```

## 5. (Beta) C Style

```c
int64_t AuthzBasepEqualUnicodeStringCaseSensitive(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((uint16_t)(*(uint16_t *)(arg1))) == (*(uint16_t *)(arg2))) goto loc_003A8A58;
    result = 0;
loc_003A8A52:
    local_rsp = (local_rsp) + (40);
    return result;
loc_003A8A58:
    result = memcmp(*(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg2 + 0x8), 0, a4);
    result = ((uint32_t)(result) == 0) ? 1 : 0;
    goto loc_003A8A52;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A8A44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003A8A44[BB_003A8A44]
  bb_003A8A50[BB_003A8A50]
  bb_003A8A52[BB_003A8A52]
  bb_003A8A57[BB_003A8A57]
  bb_003A8A58[BB_003A8A58]
  bb_003A8A44 -->|branch| bb_003A8A58
  bb_003A8A44 -->|fallthrough| bb_003A8A50
  bb_003A8A50 -->|flow| bb_003A8A52
  bb_003A8A57 -->|flow| bb_003A8A58
  bb_003A8A58 -->|branch| bb_003A8A52
```
