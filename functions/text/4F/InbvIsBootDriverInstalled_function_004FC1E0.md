# InbvIsBootDriverInstalled

- RVA: `0x004FC1E0`–`0x004FC208` (길이 `40` bytes)
- VA: `0x00000001404FC1E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004FC1F9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [DisplayBootBitmap](../53/DisplayBootBitmap_function_0053B87C.md) at `0x0053B952`
- [BvgaReleaseResources](../59/BvgaReleaseResources_function_005916E0.md) at `0x00591708`
- [StartFirstUserProcess](../../init/C7/StartFirstUserProcess_function_00C70848.md) at `0x00C70A37`

### Static image references
- `0x004FC1E4` → RVA `0x00E65E58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FC1E0  48 83 EC 28                     sub rsp, 0x28
004FC1E4  48 8B 05 6D 9C 96 00            mov rax, qword ptr [rip + 0x969c6d]
004FC1EB  48 85 C0                        test rax, rax
004FC1EE  74 10                           je 0x1404fc200
004FC1F0  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
004FC1F4  48 85 C0                        test rax, rax
004FC1F7  74 07                           je 0x1404fc200
004FC1F9  E8 D2 E8 1B 00                  call 0x1406baad0
004FC1FE  EB 02                           jmp 0x1404fc202
004FC200  32 C0                           xor al, al
004FC202  48 83 C4 28                     add rsp, 0x28
004FC206  C3                              ret
004FC207  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall InbvIsBootDriverInstalled(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 9870445) == 0) goto loc_004FC200;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9870445) + 56) == 0) goto loc_004FC200;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_004FC202;
loc_004FC200:
    result = 0;
loc_004FC202:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void InbvIsBootDriverInstalled(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x969C6D) == 0) goto loc_004FC200;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x969C6D) + 0x38) == 0) goto loc_004FC200;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_004FC202;
loc_004FC200:
    result = 0;
loc_004FC202:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FC1E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FC1E0[BB_004FC1E0]
  bb_004FC1F0[BB_004FC1F0]
  bb_004FC1F9[BB_004FC1F9]
  bb_004FC200[BB_004FC200]
  bb_004FC202[BB_004FC202]
  bb_004FC207[BB_004FC207]
  bb_004FC1E0 -->|branch| bb_004FC200
  bb_004FC1E0 -->|fallthrough| bb_004FC1F0
  bb_004FC1F0 -->|branch| bb_004FC200
  bb_004FC1F0 -->|fallthrough| bb_004FC1F9
  bb_004FC1F9 -->|branch| bb_004FC202
  bb_004FC200 -->|flow| bb_004FC202
```
