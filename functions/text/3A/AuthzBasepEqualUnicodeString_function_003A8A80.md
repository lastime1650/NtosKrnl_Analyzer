# AuthzBasepEqualUnicodeString

- RVA: `0x003A8A80`–`0x003A8AA1` (길이 `33` bytes)
- VA: `0x00000001403A8A80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `11`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003A8A8F` → [RtlEqualUnicodeString](../../page/93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x003A8A9A` → [AuthzBasepEqualUnicodeStringCaseSensitive](AuthzBasepEqualUnicodeStringCaseSensitive_function_003A8A44.md) (function, `0x003A8A44`)

### Direct callers
- [sub_00213774](../21/Unknown_function_00213774.md) at `0x00213787`
- [sub_003001D4](../30/Unknown_function_003001D4.md) at `0x003001EE`
- [AuthzBasepQueryTokenAttributeAndValues](../30/AuthzBasepQueryTokenAttributeAndValues_function_00300208.md) at `0x0030025A`
- [AuthzBasepFindSecurityAttributeValue](../30/AuthzBasepFindSecurityAttributeValue_function_00302B2C.md) at `0x00302D4E`
- [AuthzBasepFindSecurityAttributeValue](../30/AuthzBasepFindSecurityAttributeValue_function_00302B2C.md) at `0x00302DD3`
- [sub_003A7D1C](Unknown_function_003A7D1C.md) at `0x003A7D37`
- [sub_003A80B2](Unknown_function_003A80B2.md) at `0x003A80D8`
- [AuthzBasepCopyoutSecurityAttributes](AuthzBasepCopyoutSecurityAttributes_function_003A8100.md) at `0x003A83E0`
- [AuthzBasepSecurityAttributePresent](AuthzBasepSecurityAttributePresent_function_003A88B0.md) at `0x003A8964`
- [AuthzBasepFindSecurityAttribute](AuthzBasepFindSecurityAttribute_function_003A8980.md) at `0x003A8A30`
- [AuthzBasepFindSystemSecurityAttribute](../../page/9F/AuthzBasepFindSystemSecurityAttribute_function_009FF4D0.md) at `0x009FF51A`
- [AuthzBasepFindSystemSecurityAttribute](../../page/9F/AuthzBasepFindSystemSecurityAttribute_function_009FF4D0.md) at `0x009FF56C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x003A8A8F` → [RtlEqualUnicodeString](../../page/93/RtlEqualUnicodeString_function_00932A20.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A8A80  48 83 EC 28                     sub rsp, 0x28
003A8A84  44 0F 20 C0                     mov rax, cr8
003A8A88  3C 02                           cmp al, 2
003A8A8A  73 0E                           jae 0x1403a8a9a
003A8A8C  41 B0 01                        mov r8b, 1
003A8A8F  E8 8C 9F 58 00                  call 0x140932a20
003A8A94  48 83 C4 28                     add rsp, 0x28
003A8A98  C3                              ret
003A8A99  CC                              int3
003A8A9A  E8 A5 FF FF FF                  call 0x1403a8a44
003A8A9F  EB F3                           jmp 0x1403a8a94
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AuthzBasepEqualUnicodeString(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_003A8A9A;
    result = RtlEqualUnicodeString(a1, a2, 1, a4);
loc_003A8A94:
    v_rsp = (v_rsp) + (40);
    return result;
loc_003A8A9A:
    result = AuthzBasepEqualUnicodeStringCaseSensitive(a1, a2, 1, a4);
    goto loc_003A8A94;
}
```

## 5. (Beta) C Style

```c
void AuthzBasepEqualUnicodeString(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((uint8_t)(v_cr8)) >= 2) goto loc_003A8A9A;
    result = RtlEqualUnicodeString(a1, a2, 1, a4);
loc_003A8A94:
    local_rsp = (local_rsp) + (40);
    return result;
loc_003A8A9A:
    result = AuthzBasepEqualUnicodeStringCaseSensitive(a1, a2, 1, a4);
    goto loc_003A8A94;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A8A80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003A8A80[BB_003A8A80]
  bb_003A8A8C[BB_003A8A8C]
  bb_003A8A94[BB_003A8A94]
  bb_003A8A99[BB_003A8A99]
  bb_003A8A9A[BB_003A8A9A]
  bb_003A8A80 -->|branch| bb_003A8A9A
  bb_003A8A80 -->|fallthrough| bb_003A8A8C
  bb_003A8A8C -->|flow| bb_003A8A94
  bb_003A8A99 -->|flow| bb_003A8A9A
  bb_003A8A9A -->|branch| bb_003A8A94
```
