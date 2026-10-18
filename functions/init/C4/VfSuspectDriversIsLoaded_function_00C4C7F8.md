# VfSuspectDriversIsLoaded

- RVA: `0x00C4C7F8`–`0x00C4C819` (길이 `33` bytes)
- VA: `0x0000000140C4C7F8`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00C4C7FC` → [ViSuspectDriversLookupEntry](../../pagevrfy/BA/ViSuspectDriversLookupEntry_function_00BAB194.md) (function, `0x00BAB194`)

### Direct callers
- [ViDriverReApplyVerifierForAll](../../pagevrfy/B9/ViDriverReApplyVerifierForAll_function_00B9A8D4.md) at `0x00B9A935`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C4C7FC` → [ViSuspectDriversLookupEntry](../../pagevrfy/BA/ViSuspectDriversLookupEntry_function_00BAB194.md) (`INIT` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C4C7F8  48 83 EC 28                     sub rsp, 0x28
00C4C7FC  E8 93 E9 F5 FF                  call 0x140bab194
00C4C801  33 D2                           xor edx, edx
00C4C803  48 85 C0                        test rax, rax
00C4C806  74 0B                           je 0x140c4c813
00C4C808  8B 48 14                        mov ecx, dword ptr [rax + 0x14]
00C4C80B  39 48 10                        cmp dword ptr [rax + 0x10], ecx
00C4C80E  0F 97 C2                        seta dl
00C4C811  8B C2                           mov eax, edx
00C4C813  48 83 C4 28                     add rsp, 0x28
00C4C817  C3                              ret
00C4C818  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfSuspectDriversIsLoaded(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ViSuspectDriversLookupEntry(a1, a2, a3, a4);
    a2 = 0;
    if (result != 0) {
        a1 = *(unsigned int *)(result + 20);
        a2 = ((*(unsigned int *)(result + 16)) > ((unsigned int)(a1))) ? 1 : 0;
        result = a2;
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfSuspectDriversIsLoaded(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ViSuspectDriversLookupEntry(Arg1, Arg2, a3, a4);
    Arg2 = 0;
    if (result != 0) {
        Arg1 = *(uint32_t *)(result + 0x14);
        Arg2 = ((*(uint32_t *)(result + 0x10)) > ((uint32_t)(Arg1))) ? 1 : 0;
        result = Arg2;
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C4C7F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C4C7F8[BB_00C4C7F8]
  bb_00C4C808[BB_00C4C808]
  bb_00C4C813[BB_00C4C813]
  bb_00C4C818[BB_00C4C818]
  bb_00C4C7F8 -->|branch| bb_00C4C813
  bb_00C4C7F8 -->|fallthrough| bb_00C4C808
  bb_00C4C808 -->|flow| bb_00C4C813
```
