# CmOpenInstallerClassRegKey

- RVA: `0x009D4474`–`0x009D44B4` (길이 `64` bytes)
- VA: `0x00000001409D4474`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `15`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009D44A9` → [CmOpenCommonClassRegKey](../8E/CmOpenCommonClassRegKey_function_008EFF5C.md) (function, `0x008EFF5C`)

### Direct callers
- [CmCreateInstallerClassWorker](../82/CmCreateInstallerClassWorker_function_00829700.md) at `0x0082975A`
- [CmSetInstallerClassRegPropWorker](../82/CmSetInstallerClassRegPropWorker_function_0082ABF4.md) at `0x0082AD49`
- [CmDeleteInstallerClassMappedPropertyFromRegValue](../82/CmDeleteInstallerClassMappedPropertyFromRegValue_function_0082FB70.md) at `0x0082FC13`
- [_PnpDispatchInstallerClass](_PnpDispatchInstallerClass_function_009D3580.md) at `0x009D365B`
- [CmSetInstallerClassMappedPropertyFromRegValue](../AA/CmSetInstallerClassMappedPropertyFromRegValue_function_00AAEF20.md) at `0x00AAEFED`
- [sub_00B3807C](../B3/Unknown_function_00B3807C.md) at `0x00B38239`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009D4474  48 83 EC 48                     sub rsp, 0x48
009D4478  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009D4480  45 33 C9                        xor r9d, r9d
009D4483  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009D4488  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
009D4490  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009D4495  8A 44 24 78                     mov al, byte ptr [rsp + 0x78]
009D4499  45 8D 41 20                     lea r8d, [r9 + 0x20]
009D449D  88 44 24 28                     mov byte ptr [rsp + 0x28], al
009D44A1  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
009D44A5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009D44A9  E8 AE BA F1 FF                  call 0x1408eff5c
009D44AE  48 83 C4 48                     add rsp, 0x48
009D44B2  C3                              ret
009D44B3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmOpenInstallerClassRegKey(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, unsigned __int8 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int8 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    a4 = 0;
    v_stack_m10 = a8;
    v_stack_m18 = a7;
    v_stack_m20 = a6;
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    result = CmOpenCommonClassRegKey(a1, a2, a4 + 32, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmOpenInstallerClassRegKey(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, uint8_t Arg6, int64_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint8_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    Arg4 = 0;
    v_stack_m10 = Arg8;
    v_stack_m18 = Arg7;
    v_stack_m20 = Arg6;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    result = CmOpenCommonClassRegKey(Arg1, Arg2, Arg4 + 32, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009D4474&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009D4474[BB_009D4474]
  bb_009D44B3[BB_009D44B3]
```
