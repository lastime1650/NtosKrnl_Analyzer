# KeSaveIptStateBeforeProcessorGoesOffline

- RVA: `0x004D9D40`–`0x004D9D76` (길이 `54` bytes)
- VA: `0x00000001404D9D40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004D9D6B` → [KiSaveIptState](../4C/KiSaveIptState_function_004C8C44.md) (function, `0x004C8C44`)

### Direct callers
- [PnprQuiesceProcessorDpc](../../pagelk/B6/PnprQuiesceProcessorDpc_function_00B64B50.md) at `0x00B64C7C`
- [PopHandleNextState](../../pagelk/B7/PopHandleNextState_function_00B77350.md) at `0x00B77437`

### Static image references
- `0x004D9D44` → RVA `0x00FC6B94` (`ALMOSTRO`; read)
- `0x004D9D62` → RVA `0x00FC50D0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D9D40  48 83 EC 28                     sub rsp, 0x28
004D9D44  83 3D 49 CE AE 00 00            cmp dword ptr [rip + 0xaece49], 0
004D9D4B  74 23                           je 0x1404d9d70
004D9D4D  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
004D9D56  48 8B 90 D0 8F 00 00            mov rdx, qword ptr [rax + 0x8fd0]
004D9D5D  48 85 D2                        test rdx, rdx
004D9D60  74 0E                           je 0x1404d9d70
004D9D62  8B 0D 68 B3 AE 00               mov ecx, dword ptr [rip + 0xaeb368]
004D9D68  48 03 CA                        add rcx, rdx
004D9D6B  E8 D4 EE FE FF                  call 0x1404c8c44
004D9D70  48 83 C4 28                     add rsp, 0x28
004D9D74  C3                              ret
004D9D75  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeSaveIptStateBeforeProcessorGoesOffline(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 11456073)) == 0) goto loc_004D9D70;
    result = *(unsigned __int64 *)(gs_base + (0 + 32));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36816) != 0) {
        a1 = *(unsigned int *)(v_rip + 11449192);
        a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36816));
        result = KiSaveIptState(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36816), a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void KeSaveIptStateBeforeProcessorGoesOffline(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0xAECE49)) == 0) goto loc_004D9D70;
    result = *(uint64_t *)(gs_base + (0 + 0x20));
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8FD0) != 0) {
        a1 = *(uint32_t *)(v_rip + 0xAEB368);
        a1 = (a1) + (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8FD0));
        result = KiSaveIptState(a1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8FD0), a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D9D40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D9D40[BB_004D9D40]
  bb_004D9D4D[BB_004D9D4D]
  bb_004D9D62[BB_004D9D62]
  bb_004D9D70[BB_004D9D70]
  bb_004D9D75[BB_004D9D75]
  bb_004D9D40 -->|branch| bb_004D9D70
  bb_004D9D40 -->|fallthrough| bb_004D9D4D
  bb_004D9D4D -->|branch| bb_004D9D70
  bb_004D9D4D -->|fallthrough| bb_004D9D62
  bb_004D9D62 -->|flow| bb_004D9D70
```
