# Feature_CodeIntegrity_EccSupport__private_IsEnabledDeviceUsageNoInline

- RVA: `0x006A5EB0`–`0x006A5EE2` (길이 `50` bytes)
- VA: `0x00000001406A5EB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006A5ED7` → [Feature_CodeIntegrity_EccSupport__private_IsEnabledFallback](Feature_CodeIntegrity_EccSupport__private_IsEnabledFallback_function_006A5EE8.md) (function, `0x006A5EE8`)

### Direct callers
- [MinCryptVerifySignedHash2](../../page/83/MinCryptVerifySignedHash2_function_008362A0.md) at `0x00836351`
- [HashpVerifyEcdsaSignature](../../page/84/HashpVerifyEcdsaSignature_function_00841AF4.md) at `0x00841B29`
- [HashpVerifyEcdsaSignature](../../page/84/HashpVerifyEcdsaSignature_function_00841AF4.md) at `0x00841BBB`

### Static image references
- `0x006A5EBA` → RVA `0x00FC4AA0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A5EB0  48 83 EC 28                     sub rsp, 0x28
006A5EB4  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
006A5EBA  8B 05 E0 EB 91 00               mov eax, dword ptr [rip + 0x91ebe0]
006A5EC0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006A5EC4  A8 10                           test al, 0x10
006A5EC6  74 05                           je 0x1406a5ecd
006A5EC8  83 E0 01                        and eax, 1
006A5ECB  EB 0F                           jmp 0x1406a5edc
006A5ECD  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
006A5ED2  BA 03 00 00 00                  mov edx, 3
006A5ED7  E8 0C 00 00 00                  call 0x1406a5ee8
006A5EDC  48 83 C4 28                     add rsp, 0x28
006A5EE0  C3                              ret
006A5EE1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_CodeIntegrity_EccSupport__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9563104)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9563104)))) & (16)) == 0) goto loc_006A5ECD;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9563104))) & (1));
    goto loc_006A5EDC;
loc_006A5ECD:
    result = Feature_CodeIntegrity_EccSupport__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_006A5EDC:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_CodeIntegrity_EccSupport__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x91EBE0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x91EBE0)))) & (16)) == 0) goto loc_006A5ECD;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x91EBE0))) & (1));
    goto loc_006A5EDC;
loc_006A5ECD:
    result = Feature_CodeIntegrity_EccSupport__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_006A5EDC:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A5EB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006A5EB0[BB_006A5EB0]
  bb_006A5EC8[BB_006A5EC8]
  bb_006A5ECD[BB_006A5ECD]
  bb_006A5EDC[BB_006A5EDC]
  bb_006A5EE1[BB_006A5EE1]
  bb_006A5EB0 -->|branch| bb_006A5ECD
  bb_006A5EB0 -->|fallthrough| bb_006A5EC8
  bb_006A5EC8 -->|branch| bb_006A5EDC
  bb_006A5ECD -->|flow| bb_006A5EDC
```
