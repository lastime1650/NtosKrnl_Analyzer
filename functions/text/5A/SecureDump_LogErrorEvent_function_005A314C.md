# SecureDump_LogErrorEvent

- RVA: `0x005A314C`–`0x005A3175` (길이 `41` bytes)
- VA: `0x00000001405A314C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005A316A` → [McTemplateK0q_EtwWriteTransfer](../59/McTemplateK0q_EtwWriteTransfer_function_00596B68.md) (function, `0x00596B68`)

### Direct callers
- [SecureDump_EncryptSymmetricKeyWithPublicKey](SecureDump_EncryptSymmetricKeyWithPublicKey_function_005A27A4.md) at `0x005A29F2`
- [SecureDump_LoadCertAndProvisionKey](SecureDump_LoadCertAndProvisionKey_function_005A2E04.md) at `0x005A3035`
- [SecureDump_LoadCertAndProvisionKey](SecureDump_LoadCertAndProvisionKey_function_005A2E04.md) at `0x005A30E1`
- [SecureDump_PrepareForInit](SecureDump_PrepareForInit_function_005A317C.md) at `0x005A339D`
- [SecureDump_SymmetricEncryptionSetup](SecureDump_SymmetricEncryptionSetup_function_005A3774.md) at `0x005A3899`

### Static image references
- `0x005A3150` → RVA `0x00F8D8D4` (`.data`; read)
- `0x005A315C` → RVA `0x00021A30` (`.rdata`; read)
- `0x005A3163` → RVA `0x00E06E20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A314C  48 83 EC 28                     sub rsp, 0x28
005A3150  F6 05 7D A7 9E 00 04            test byte ptr [rip + 0x9ea77d], 4
005A3157  74 16                           je 0x1405a316f
005A3159  44 8B C9                        mov r9d, ecx
005A315C  48 8D 15 CD E8 A7 FF            lea rdx, [rip - 0x581733]
005A3163  48 8D 0D B6 3C 86 00            lea rcx, [rip + 0x863cb6]
005A316A  E8 F9 39 FF FF                  call 0x140596b68
005A316F  48 83 C4 28                     add rsp, 0x28
005A3173  C3                              ret
005A3174  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SecureDump_LogErrorEvent(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned __int8 *)(v_rip + 10397565)) & (4)) != 0) {
        a4 = a1;
        a2 = v_rip - 5773107;
        a1 = v_rip + 8797366;
        result = McTemplateK0q_EtwWriteTransfer(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SecureDump_LogErrorEvent(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint8_t *)(v_rip + 0x9EA77D)) & (4)) != 0) {
        a4 = Arg1;
        a2 = v_rip - 5773107;
        Arg1 = v_rip + 8797366;
        result = McTemplateK0q_EtwWriteTransfer(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A314C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005A314C[BB_005A314C]
  bb_005A3159[BB_005A3159]
  bb_005A316F[BB_005A316F]
  bb_005A3174[BB_005A3174]
  bb_005A314C -->|branch| bb_005A316F
  bb_005A314C -->|fallthrough| bb_005A3159
  bb_005A3159 -->|flow| bb_005A316F
```
