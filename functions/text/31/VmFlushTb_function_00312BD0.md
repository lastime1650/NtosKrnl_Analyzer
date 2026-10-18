# VmFlushTb

- RVA: `0x00312BD0`–`0x00312C0A` (길이 `58` bytes)
- VA: `0x0000000140312BD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `15`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00312BFF` → [VmpFlushTb](VmpFlushTb_function_00311BD0.md) (function, `0x00311BD0`)

### Direct callers
- [sub_003120A5](Unknown_function_003120A5.md) at `0x0031215F`
- [KeFlushSingleCurrentTb](../5B/KeFlushSingleCurrentTb_function_005BDC9C.md) at `0x005BDDF4`
- [KeFlushSingleTb](../5B/KeFlushSingleTb_function_005BDE84.md) at `0x005BDFEF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00312BD0  48 83 EC 28                     sub rsp, 0x28
00312BD4  44 8B C9                        mov r9d, ecx
00312BD7  41 83 F8 01                     cmp r8d, 1
00312BDB  75 27                           jne 0x140312c04
00312BDD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00312BE6  4C 8B 80 B8 00 00 00            mov r8, qword ptr [rax + 0xb8]
00312BED  49 8B 88 70 06 00 00            mov rcx, qword ptr [r8 + 0x670]
00312BF4  48 85 C9                        test rcx, rcx
00312BF7  74 0B                           je 0x140312c04
00312BF9  4C 8B C2                        mov r8, rdx
00312BFC  41 8B D1                        mov edx, r9d
00312BFF  E8 CC EF FF FF                  call 0x140311bd0
00312C04  48 83 C4 28                     add rsp, 0x28
00312C08  C3                              ret
00312C09  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmFlushTb(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 != 1) goto loc_00312C04;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1648) != 0) {
        a3 = a2;
        a2 = (unsigned int)((unsigned int)(a1));
        result = VmpFlushTb(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1648), a2, a3, (unsigned int)(a1));
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VmFlushTb(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 != 1) goto loc_00312C04;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x670) != 0) {
        Arg3 = Arg2;
        Arg2 = (uint32_t)((uint32_t)(Arg1));
        result = VmpFlushTb(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x670), Arg2, Arg3, (uint32_t)(Arg1));
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00312BD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00312BD0[BB_00312BD0]
  bb_00312BDD[BB_00312BDD]
  bb_00312BF9[BB_00312BF9]
  bb_00312C04[BB_00312C04]
  bb_00312C09[BB_00312C09]
  bb_00312BD0 -->|branch| bb_00312C04
  bb_00312BD0 -->|fallthrough| bb_00312BDD
  bb_00312BDD -->|branch| bb_00312C04
  bb_00312BDD -->|fallthrough| bb_00312BF9
  bb_00312BF9 -->|flow| bb_00312C04
```
