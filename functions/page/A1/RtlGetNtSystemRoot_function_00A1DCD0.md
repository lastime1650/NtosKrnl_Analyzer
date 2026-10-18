# RtlGetNtSystemRoot

- RVA: `0x00A1DCD0`–`0x00A1DCFF` (길이 `47` bytes)
- VA: `0x0000000140A1DCD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A1AC`
- 디코드: `12`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A1DCD4` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00A1DCED` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- [SdbpGetManifestedMergeStubAlloc](../81/SdbpGetManifestedMergeStubAlloc_function_0081275C.md) at `0x008129D1`
- [AslEnvVarQuery](../81/AslEnvVarQuery_function_0081D410.md) at `0x0081D458`
- [ObpLookupObjectName](../89/ObpLookupObjectName_function_0089BE90.md) at `0x0089C523`
- [MiCacheImageSymbols](../AD/MiCacheImageSymbols_function_00AD9410.md) at `0x00AD94FB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A1DCD4` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00A1DCED` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A1DCD0  48 83 EC 28                     sub rsp, 0x28
00A1DCD4  E8 07 86 A1 FF                  call 0x1404362e0
00A1DCD9  84 C0                           test al, al
00A1DCDB  75 10                           jne 0x140a1dced
00A1DCDD  48 B8 30 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000030
00A1DCE7  48 83 C4 28                     add rsp, 0x28
00A1DCEB  C3                              ret
00A1DCEC  CC                              int3
00A1DCED  E8 FE 04 8E FF                  call 0x1402fe1f0
00A1DCF2  48 8B 80 08 05 00 00            mov rax, qword ptr [rax + 0x508]
00A1DCF9  48 83 C0 1E                     add rax, 0x1e
00A1DCFD  EB E8                           jmp 0x140a1dce7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlGetNtSystemRoot(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A1DCED;
loc_00A1DCE7:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A1DCED:
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    result = (*(unsigned __int64 *)(result + 1288)) + (30);
    goto loc_00A1DCE7;
}
```

## 5. (Beta) C Style

```c
void RtlGetNtSystemRoot(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00A1DCED;
loc_00A1DCE7:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A1DCED:
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    result = (*(uint64_t *)(result + 0x508)) + (30);
    goto loc_00A1DCE7;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A1DCD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A1DCD0[BB_00A1DCD0]
  bb_00A1DCDD[BB_00A1DCDD]
  bb_00A1DCE7[BB_00A1DCE7]
  bb_00A1DCEC[BB_00A1DCEC]
  bb_00A1DCED[BB_00A1DCED]
  bb_00A1DCD0 -->|branch| bb_00A1DCED
  bb_00A1DCD0 -->|fallthrough| bb_00A1DCDD
  bb_00A1DCDD -->|flow| bb_00A1DCE7
  bb_00A1DCEC -->|flow| bb_00A1DCED
  bb_00A1DCED -->|branch| bb_00A1DCE7
```
