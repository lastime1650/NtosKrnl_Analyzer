# PopPulseSystemIdleEvent

- RVA: `0x00A31B8C`–`0x00A31BD1` (길이 `69` bytes)
- VA: `0x0000000140A31B8C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `17`개 명령, `69/69` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopUpdateSystemIdleContext](../91/PopUpdateSystemIdleContext_function_00911BB4.md) at `0x00911D02`
- [PopSystemIdleWorker](PopSystemIdleWorker_function_00A31A60.md) at `0x00A31A93`
- [PopUpdateLastUserInputTime](PopUpdateLastUserInputTime_function_00A31E24.md) at `0x00A31E6C`
- [PopInitializeSystemIdleDetection](../../init/C4/PopInitializeSystemIdleDetection_function_00C408EC.md) at `0x00C40901`

### Static image references
- `0x00A31BB9` → RVA `0x00E0B6D0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A31B8C  45 33 C0                        xor r8d, r8d
00A31B8F  83 F9 03                        cmp ecx, 3
00A31B92  77 35                           ja 0x140a31bc9
00A31B94  48 BA 08 00 00 00 80 F7 FF FF   movabs rdx, 0xfffff78000000008
00A31B9E  48 B8 BD 42 7A E5 D5 94 BF D6   movabs rax, 0xd6bf94d5e57a42bd
00A31BA8  48 8B 12                        mov rdx, qword ptr [rdx]
00A31BAB  48 F7 E2                        mul rdx
00A31BAE  48 63 C1                        movsxd rax, ecx
00A31BB1  48 C1 EA 17                     shr rdx, 0x17
00A31BB5  48 6B C8 38                     imul rcx, rax, 0x38
00A31BB9  48 8D 05 10 9B 3D 00            lea rax, [rip + 0x3d9b10]
00A31BC0  48 89 14 01                     mov qword ptr [rcx + rax], rdx
00A31BC4  41 8B C0                        mov eax, r8d
00A31BC7  C3                              ret
00A31BC8  CC                              int3
00A31BC9  41 B8 0D 00 00 C0               mov r8d, 0xc000000d
00A31BCF  EB F3                           jmp 0x140a31bc4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPulseSystemIdleEvent(int a1, __int64 a2, int a3)
{
    a3 = 0;
    if (a1 > 3) goto loc_00A31BC9;
    a2 = (*(unsigned __int64 *)(a2)) >> (23);
    a1 = (a1) * ((int)(a1));
    *(unsigned __int64 *)(a1 + v_rip + 4037392 * 1) = a2;
loc_00A31BC4:
    return 0;
loc_00A31BC9:
    goto loc_00A31BC4;
}
```

## 5. (Beta) C Style

```c
int64_t PopPulseSystemIdleEvent(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    Arg3 = 0;
    if (Arg1 > 3) goto loc_00A31BC9;
    Arg2 = (*(uint64_t *)(Arg2)) >> (23);
    Arg1 = (Arg1) * ((int32_t)(Arg1));
    *(uint64_t *)(Arg1 + v_rip + 0x3D9B10 * 1) = Arg2;
loc_00A31BC4:
    return 0;
loc_00A31BC9:
    goto loc_00A31BC4;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A31B8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A31B8C[BB_00A31B8C]
  bb_00A31B94[BB_00A31B94]
  bb_00A31BC4[BB_00A31BC4]
  bb_00A31BC8[BB_00A31BC8]
  bb_00A31BC9[BB_00A31BC9]
  bb_00A31B8C -->|branch| bb_00A31BC9
  bb_00A31B8C -->|fallthrough| bb_00A31B94
  bb_00A31B94 -->|flow| bb_00A31BC4
  bb_00A31BC8 -->|flow| bb_00A31BC9
  bb_00A31BC9 -->|branch| bb_00A31BC4
```
