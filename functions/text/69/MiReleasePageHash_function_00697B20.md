# MiReleasePageHash

- RVA: `0x00697B20`–`0x00697B79` (길이 `89` bytes)
- VA: `0x0000000140697B20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `19`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00697B6E` → [MiReleasePtes](../24/MiReleasePtes_function_00247240.md) (function, `0x00247240`)

### Direct callers
- [MiAttemptChangePagingFileMaximum](../67/MiAttemptChangePagingFileMaximum_function_0067FE7C.md) at `0x0067FEDE`
- [MiDeletePagefile](../../page/7F/MiDeletePagefile_function_007FFB88.md) at `0x007FFBEA`

### Static image references
- `0x00697B24` → RVA `0x00E3738C` (`.data`; read)
- `0x00697B67` → RVA `0x00E37668` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00697B20  48 83 EC 28                     sub rsp, 0x28
00697B24  44 8B 0D 61 F8 79 00            mov r9d, dword ptr [rip + 0x79f861]
00697B2B  41 B8 00 00 00 00               mov r8d, 0
00697B31  8B C2                           mov eax, edx
00697B33  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
00697B3D  4C 0F AF C8                     imul r9, rax
00697B41  49 F7 C1 FF 0F 00 00            test r9, 0xfff
00697B48  41 0F 95 C0                     setne r8b
00697B4C  49 C1 E9 0C                     shr r9, 0xc
00697B50  48 C1 E9 09                     shr rcx, 9
00697B54  45 03 C1                        add r8d, r9d
00697B57  48 23 D1                        and rdx, rcx
00697B5A  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00697B64  48 03 D0                        add rdx, rax
00697B67  48 8D 0D FA FA 79 00            lea rcx, [rip + 0x79fafa]
00697B6E  E8 CD F6 BA FF                  call 0x140247240
00697B73  48 83 C4 28                     add rsp, 0x28
00697B77  C3                              ret
00697B78  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReleasePageHash(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = ((unsigned int)(*(unsigned int *)(v_rip + 7993441))) * ((unsigned int)(a2));
    a3 = (((a4) & (0xFFFULL)) != 0) ? 1 : 0;
    a4 = (a4) >> (12);
    a1 = (a1) >> (9);
    a3 = (unsigned int)((a3) + ((unsigned int)(a4)));
    a2 = (a2) & (a1);
    a2 = (a2) + ((unsigned int)(a2));
    result = MiReleasePtes(v_rip + 7994106, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReleasePageHash(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    a4 = ((uint32_t)(*(uint32_t *)(v_rip + 0x79F861))) * ((uint32_t)(Arg2));
    a3 = (((a4) & (0xFFFULL)) != 0) ? 1 : 0;
    a4 = (a4) >> (12);
    Arg1 = (Arg1) >> (9);
    a3 = (uint32_t)((a3) + ((uint32_t)(a4)));
    Arg2 = (Arg2) & (Arg1);
    Arg2 = (Arg2) + ((uint32_t)(Arg2));
    result = MiReleasePtes(v_rip + 7994106, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00697B20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00697B20[BB_00697B20]
  bb_00697B78[BB_00697B78]
```
