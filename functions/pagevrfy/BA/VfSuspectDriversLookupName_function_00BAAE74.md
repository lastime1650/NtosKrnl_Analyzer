# VfSuspectDriversLookupName

- RVA: `0x00BAAE74`–`0x00BAAE8D` (길이 `25` bytes)
- VA: `0x0000000140BAAE74`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BAAE78` → [ViSuspectDriversLookupEntry](ViSuspectDriversLookupEntry_function_00BAB194.md) (function, `0x00BAB194`)

### Direct callers
- [VfDriverApplyDifVerification](../B9/VfDriverApplyDifVerification_function_00B9A028.md) at `0x00B9A05B`
- [VfDriverEnableVerifier](../B9/VfDriverEnableVerifier_function_00B9A240.md) at `0x00B9A27C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAAE74  48 83 EC 28                     sub rsp, 0x28
00BAAE78  E8 17 03 00 00                  call 0x140bab194
00BAAE7D  33 C9                           xor ecx, ecx
00BAAE7F  48 85 C0                        test rax, rax
00BAAE82  0F 95 C1                        setne cl
00BAAE85  8B C1                           mov eax, ecx
00BAAE87  48 83 C4 28                     add rsp, 0x28
00BAAE8B  C3                              ret
00BAAE8C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfSuspectDriversLookupName(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ViSuspectDriversLookupEntry(a1, a2, a3, a4);
    a1 = 0;
    a1 = (result != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(a1);
}
```

## 5. (Beta) C Style

```c
int64_t VfSuspectDriversLookupName(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ViSuspectDriversLookupEntry(Arg1, a2, a3, a4);
    Arg1 = 0;
    Arg1 = (result != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(Arg1);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAAE74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAAE74[BB_00BAAE74]
  bb_00BAAE8C[BB_00BAAE8C]
```
