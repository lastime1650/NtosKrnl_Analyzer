# ZwQuerySecurityObject

- RVA: `0x006AFDF0`–`0x006AFE0F` (길이 `31` bytes)
- VA: `0x00000001406AFDF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0F7C`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [DifZwQuerySecurityObjectWrapper](../64/DifZwQuerySecurityObjectWrapper_function_00648590.md) at `0x0064869A`
- [sub_006F7D0E](../6F/Unknown_function_006F7D0E.md) at `0x006F7D2A`
- [sub_006F7D0E](../6F/Unknown_function_006F7D0E.md) at `0x006F7D81`
- [CmpSaveBootControlSet](../../page/7D/CmpSaveBootControlSet_function_007DC744.md) at `0x007DC859`
- [CmpSaveBootControlSet](../../page/7D/CmpSaveBootControlSet_function_007DC744.md) at `0x007DC89F`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E3197`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E31D9`
- [RegRtlGetKeySecurity](../../page/83/RegRtlGetKeySecurity_function_008329F4.md) at `0x00832A03`
- [CmpQueryFileSecurityDescriptor](../../page/87/CmpQueryFileSecurityDescriptor_function_0087B318.md) at `0x0087B349`
- [CmpQueryFileSecurityDescriptor](../../page/87/CmpQueryFileSecurityDescriptor_function_0087B318.md) at `0x0087B387`
- [PiDevCfgGetKeySecurityDescriptor](../../page/99/PiDevCfgGetKeySecurityDescriptor_function_00996240.md) at `0x009962BD`
- [PiDevCfgGetKeySecurityDescriptor](../../page/99/PiDevCfgGetKeySecurityDescriptor_function_00996240.md) at `0x0099635A`

### Static image references
- `0x006AFDFC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AFE09` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AFDF0  48 8B C4                        mov rax, rsp
006AFDF3  FA                              cli
006AFDF4  48 83 EC 10                     sub rsp, 0x10
006AFDF8  50                              push rax
006AFDF9  9C                              pushfq
006AFDFA  6A 10                           push 0x10
006AFDFC  48 8D 05 5D 36 00 00            lea rax, [rip + 0x365d]
006AFE03  50                              push rax
006AFE04  B8 69 01 00 00                  mov eax, 0x169
006AFE09  E9 B2 4B 01 00                  jmp 0x1406c49c0
006AFE0E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwQuerySecurityObject(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwQuerySecurityObject(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AFDF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AFDF0[BB_006AFDF0]
  bb_006AFE0E[BB_006AFE0E]
```
