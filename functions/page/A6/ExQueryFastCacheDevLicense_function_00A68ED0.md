# ExQueryFastCacheDevLicense

- RVA: `0x00A68ED0`–`0x00A68EFB` (길이 `43` bytes)
- VA: `0x0000000140A68ED0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A68EE1` → [KIsDeveloperModeEnabled](KIsDeveloperModeEnabled_function_00A68F04.md) (function, `0x00A68F04`)

### Direct callers
- [SepIsLockedDown](../79/SepIsLockedDown_function_0079BC28.md) at `0x0079BCAA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A68ED0  40 53                           push rbx
00A68ED2  48 83 EC 20                     sub rsp, 0x20
00A68ED6  33 DB                           xor ebx, ebx
00A68ED8  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00A68EDD  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
00A68EE1  E8 1E 00 00 00                  call 0x140a68f04
00A68EE6  85 C0                           test eax, eax
00A68EE8  78 08                           js 0x140a68ef2
00A68EEA  38 5C 24 30                     cmp byte ptr [rsp + 0x30], bl
00A68EEE  74 02                           je 0x140a68ef2
00A68EF0  B3 01                           mov bl, 1
00A68EF2  8A C3                           mov al, bl
00A68EF4  48 83 C4 20                     add rsp, 0x20
00A68EF8  5B                              pop rbx
00A68EF9  C3                              ret
00A68EFA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExQueryFastCacheDevLicense(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    v_stack_p8 = 0;
    result = KIsDeveloperModeEnabled(v_stack_p8, a2, a3, a4);
    if (sign_flag) goto loc_00A68EF2;
    if (v_stack_p8 != 0) {
        v_rbx = 1;
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_rbx);
}
```

## 5. (Beta) C Style

```c
void ExQueryFastCacheDevLicense(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    v_stack_p8 = 0;
    result = KIsDeveloperModeEnabled(v_stack_p8, a2, a3, a4);
    if (sign_flag) goto loc_00A68EF2;
    if (v_stack_p8 != 0) {
        local_rbx = 1;
    }
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(local_rbx);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A68ED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A68ED0[BB_00A68ED0]
  bb_00A68EEA[BB_00A68EEA]
  bb_00A68EF0[BB_00A68EF0]
  bb_00A68EF2[BB_00A68EF2]
  bb_00A68EFA[BB_00A68EFA]
  bb_00A68ED0 -->|branch| bb_00A68EF2
  bb_00A68ED0 -->|fallthrough| bb_00A68EEA
  bb_00A68EEA -->|branch| bb_00A68EF2
  bb_00A68EEA -->|fallthrough| bb_00A68EF0
  bb_00A68EF0 -->|flow| bb_00A68EF2
```
