# VfUtilIsBootDriver

- RVA: `0x00B933D0`–`0x00B933EC` (길이 `28` bytes)
- VA: `0x0000000140B933D0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B933D4` → [VfTargetDriversGetVerifierData](../BB/VfTargetDriversGetVerifierData_function_00BB7E6C.md) (function, `0x00BB7E6C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B933D0  48 83 EC 28                     sub rsp, 0x28
00B933D4  E8 93 4A 02 00                  call 0x140bb7e6c
00B933D9  48 85 C0                        test rax, rax
00B933DC  74 08                           je 0x140b933e6
00B933DE  8B 40 20                        mov eax, dword ptr [rax + 0x20]
00B933E1  D1 E8                           shr eax, 1
00B933E3  83 E0 01                        and eax, 1
00B933E6  48 83 C4 28                     add rsp, 0x28
00B933EA  C3                              ret
00B933EB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfUtilIsBootDriver(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = VfTargetDriversGetVerifierData(a1, a2, a3, a4);
    if (result != 0) {
        result = *(unsigned int *)(result + 32);
        result = (unsigned int)((result) >> (1));
        result = (unsigned int)((result) & (1));
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void VfUtilIsBootDriver(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = VfTargetDriversGetVerifierData(a1, a2, a3, a4);
    if (result != 0) {
        result = *(uint32_t *)(result + 0x20);
        result = (uint32_t)((result) >> (1));
        result = (uint32_t)((result) & (1));
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B933D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B933D0[BB_00B933D0]
  bb_00B933DE[BB_00B933DE]
  bb_00B933E6[BB_00B933E6]
  bb_00B933EB[BB_00B933EB]
  bb_00B933D0 -->|branch| bb_00B933E6
  bb_00B933D0 -->|fallthrough| bb_00B933DE
  bb_00B933DE -->|flow| bb_00B933E6
```
