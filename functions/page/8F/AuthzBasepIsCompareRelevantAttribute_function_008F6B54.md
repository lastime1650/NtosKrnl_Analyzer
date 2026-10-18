# AuthzBasepIsCompareRelevantAttribute

- RVA: `0x008F6B54`–`0x008F6B81` (길이 `45` bytes)
- VA: `0x00000001408F6B54`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `15`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008F6B6D` → [RtlPrefixUnicodeString](RtlPrefixUnicodeString_function_008F4F70.md) (function, `0x008F4F70`)

### Direct callers
- [AuthzBasepCompareLegacySecurityAttributesInformation](AuthzBasepCompareLegacySecurityAttributesInformation_function_008F7374.md) at `0x008F73A8`
- [AuthzBasepCompareLegacySecurityAttributesInformation](AuthzBasepCompareLegacySecurityAttributesInformation_function_008F7374.md) at `0x008F7402`

### Static image references
- `0x008F6B66` → RVA `0x00001C40` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008F6B54  48 83 EC 28                     sub rsp, 0x28
008F6B58  8B 41 34                        mov eax, dword ptr [rcx + 0x34]
008F6B5B  A8 40                           test al, 0x40
008F6B5D  75 1E                           jne 0x1408f6b7d
008F6B5F  48 8D 51 20                     lea rdx, [rcx + 0x20]
008F6B63  41 B0 01                        mov r8b, 1
008F6B66  48 8D 0D D3 B0 70 FF            lea rcx, [rip - 0x8f4f2d]
008F6B6D  E8 FE E3 FF FF                  call 0x1408f4f70
008F6B72  84 C0                           test al, al
008F6B74  0F 94 C0                        sete al
008F6B77  48 83 C4 28                     add rsp, 0x28
008F6B7B  C3                              ret
008F6B7C  CC                              int3
008F6B7D  32 C0                           xor al, al
008F6B7F  EB F6                           jmp 0x1408f6b77
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AuthzBasepIsCompareRelevantAttribute(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 52)))) & (64)) != 0) goto loc_008F6B7D;
    result = RtlPrefixUnicodeString(v_rip - 9391917, a1 + 32, 1, a4);
    result = ((unsigned __int8)(result) == 0) ? 1 : 0;
loc_008F6B77:
    v_rsp = (v_rsp) + (40);
    return result;
loc_008F6B7D:
    result = 0;
    goto loc_008F6B77;
}
```

## 5. (Beta) C Style

```c
int64_t AuthzBasepIsCompareRelevantAttribute(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x34)))) & (64)) != 0) goto loc_008F6B7D;
    result = RtlPrefixUnicodeString(v_rip - 9391917, Arg1 + 32, 1, a4);
    result = ((uint8_t)(result) == 0) ? 1 : 0;
loc_008F6B77:
    local_rsp = (local_rsp) + (40);
    return result;
loc_008F6B7D:
    result = 0;
    goto loc_008F6B77;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x34` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F6B54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008F6B54[BB_008F6B54]
  bb_008F6B5F[BB_008F6B5F]
  bb_008F6B77[BB_008F6B77]
  bb_008F6B7C[BB_008F6B7C]
  bb_008F6B7D[BB_008F6B7D]
  bb_008F6B54 -->|branch| bb_008F6B7D
  bb_008F6B54 -->|fallthrough| bb_008F6B5F
  bb_008F6B5F -->|flow| bb_008F6B77
  bb_008F6B7C -->|flow| bb_008F6B7D
  bb_008F6B7D -->|branch| bb_008F6B77
```
