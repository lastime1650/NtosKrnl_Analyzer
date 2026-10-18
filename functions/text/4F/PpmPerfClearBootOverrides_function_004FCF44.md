# PpmPerfClearBootOverrides

- RVA: `0x004FCF44`–`0x004FCF7C` (길이 `56` bytes)
- VA: `0x00000001404FCF44`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `15`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x004FCF67` → [PpmAcquireLock](../2D/PpmAcquireLock_function_002D9AA4.md) (function, `0x002D9AA4`)
- `0x004FCF71` → [PpmReinitializeHeteroEngine](../../page/A5/PpmReinitializeHeteroEngine_function_00A53108.md) (function, `0x00A53108`)

### Direct callers
- [PopSetupHighPerfPowerRequest](../../page/75/PopSetupHighPerfPowerRequest_function_00753AE0.md) at `0x00753AF1`
- [PopPowerRequestCallbackPerfBoostRequired](../../page/A9/PopPowerRequestCallbackPerfBoostRequired_function_00A96F70.md) at `0x00A96F7E`

### Static image references
- `0x004FCF4A` → RVA `0x00FC5180` (`ALMOSTRO`; read)
- `0x004FCF52` → RVA `0x00FC6B40` (`ALMOSTRO`; read)
- `0x004FCF58` → RVA `0x00FC5180` (`ALMOSTRO`; write)
- `0x004FCF60` → RVA `0x00F0CC00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004FCF71` → [PpmReinitializeHeteroEngine](../../page/A5/PpmReinitializeHeteroEngine_function_00A53108.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FCF44  48 83 EC 28                     sub rsp, 0x28
004FCF48  33 C0                           xor eax, eax
004FCF4A  39 05 30 82 AC 00               cmp dword ptr [rip + 0xac8230], eax
004FCF50  74 24                           je 0x1404fcf76
004FCF52  39 05 E8 9B AC 00               cmp dword ptr [rip + 0xac9be8], eax
004FCF58  89 05 22 82 AC 00               mov dword ptr [rip + 0xac8222], eax
004FCF5E  74 16                           je 0x1404fcf76
004FCF60  48 8D 0D 99 FC A0 00            lea rcx, [rip + 0xa0fc99]
004FCF67  E8 38 CB DD FF                  call 0x1402d9aa4
004FCF6C  45 33 C0                        xor r8d, r8d
004FCF6F  33 C9                           xor ecx, ecx
004FCF71  E8 92 61 55 00                  call 0x140a53108
004FCF76  48 83 C4 28                     add rsp, 0x28
004FCF7A  C3                              ret
004FCF7B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmPerfClearBootOverrides(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if ((*(unsigned int *)(v_rip + 11305520)) == 0) goto loc_004FCF76;
    *(unsigned int *)(v_rip + 11305506) = 0;
    if ((*(unsigned int *)(v_rip + 11312104)) != 0) {
        a1 = v_rip + 10550425;
        result = PpmAcquireLock(a1, a2, a3, a4);
        a3 = 0;
        a1 = 0;
        result = PpmReinitializeHeteroEngine(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmPerfClearBootOverrides(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if ((*(uint32_t *)(v_rip + 0xAC8230)) == 0) goto loc_004FCF76;
    *(uint32_t *)(v_rip + 0xAC8222) = 0;
    if ((*(uint32_t *)(v_rip + 0xAC9BE8)) != 0) {
        Arg1 = v_rip + 10550425;
        result = PpmAcquireLock(Arg1, Arg2, Arg3, a4);
        Arg3 = 0;
        Arg1 = 0;
        result = PpmReinitializeHeteroEngine(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FCF44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FCF44[BB_004FCF44]
  bb_004FCF52[BB_004FCF52]
  bb_004FCF60[BB_004FCF60]
  bb_004FCF76[BB_004FCF76]
  bb_004FCF7B[BB_004FCF7B]
  bb_004FCF44 -->|branch| bb_004FCF76
  bb_004FCF44 -->|fallthrough| bb_004FCF52
  bb_004FCF52 -->|branch| bb_004FCF76
  bb_004FCF52 -->|fallthrough| bb_004FCF60
  bb_004FCF60 -->|flow| bb_004FCF76
```
