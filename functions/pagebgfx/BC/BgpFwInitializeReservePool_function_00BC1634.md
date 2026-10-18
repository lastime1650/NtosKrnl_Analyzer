# BgpFwInitializeReservePool

- RVA: `0x00BC1634`–`0x00BC1670` (길이 `60` bytes)
- VA: `0x0000000140BC1634`
- 실행 섹션: `PAGEBGFX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00BC1665` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (function, `0x00450230`)

### Direct callers
- [BgpFwLibraryDestroy](BgpFwLibraryDestroy_function_00BC1678.md) at `0x00BC16E3`
- [BgpFwReservePoolSwap](BgpFwReservePoolSwap_function_00BC1828.md) at `0x00BC18B0`
- [BgpFwLibraryInitialize](BgpFwLibraryInitialize_function_00BC5400.md) at `0x00BC5582`
- [BgpFwLibraryInitialize](BgpFwLibraryInitialize_function_00BC5400.md) at `0x00BC58E9`

### Static image references
- `0x00BC1638` → RVA `0x00E3EE34` (`.data`; read/write)
- `0x00BC163F` → RVA `0x00E62388` (`.data`; write)
- `0x00BC1646` → RVA `0x00E3EE38` (`.data`; write)
- `0x00BC164C` → RVA `0x00E64F58` (`.data`; write)
- `0x00BC1652` → RVA `0x00E64F60` (`.data`; write)
- `0x00BC165E` → RVA `0x00E64F58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BC1665` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (`PAGEBGFX` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC1634  48 83 EC 28                     sub rsp, 0x28
00BC1638  83 25 F5 D7 27 00 00            and dword ptr [rip + 0x27d7f5], 0
00BC163F  48 89 0D 42 0D 2A 00            mov qword ptr [rip + 0x2a0d42], rcx
00BC1646  89 15 EC D7 27 00               mov dword ptr [rip + 0x27d7ec], edx
00BC164C  89 15 06 39 2A 00               mov dword ptr [rip + 0x2a3906], edx
00BC1652  4C 89 05 07 39 2A 00            mov qword ptr [rip + 0x2a3907], r8
00BC1659  4D 85 C0                        test r8, r8
00BC165C  74 0C                           je 0x140bc166a
00BC165E  48 8D 0D F3 38 2A 00            lea rcx, [rip + 0x2a38f3]
00BC1665  E8 C6 EB 88 FF                  call 0x140450230
00BC166A  48 83 C4 28                     add rsp, 0x28
00BC166E  C3                              ret
00BC166F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgpFwInitializeReservePool(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(v_rip + 2755906) = a1;
    *(unsigned int *)(v_rip + 2611180) = a2;
    *(unsigned int *)(v_rip + 2767110) = a2;
    *(unsigned __int64 *)(v_rip + 2767111) = a3;
    if (a3 != 0) {
        a1 = v_rip + 2767091;
        result = RtlClearAllBits(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t BgpFwInitializeReservePool(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint64_t *)(v_rip + 0x2A0D42) = Arg1;
    *(uint32_t *)(v_rip + 0x27D7EC) = Arg2;
    *(uint32_t *)(v_rip + 0x2A3906) = Arg2;
    *(uint64_t *)(v_rip + 0x2A3907) = Arg3;
    if (Arg3 != 0) {
        Arg1 = v_rip + 2767091;
        result = RtlClearAllBits(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagebgfx&rva=0x00BC1634&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC1634[BB_00BC1634]
  bb_00BC165E[BB_00BC165E]
  bb_00BC166A[BB_00BC166A]
  bb_00BC166F[BB_00BC166F]
  bb_00BC1634 -->|branch| bb_00BC166A
  bb_00BC1634 -->|fallthrough| bb_00BC165E
  bb_00BC165E -->|flow| bb_00BC166A
```
