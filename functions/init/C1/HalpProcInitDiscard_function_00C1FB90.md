# HalpProcInitDiscard

- RVA: `0x00C1FB90`–`0x00C1FBED` (길이 `93` bytes)
- VA: `0x0000000140C1FB90`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `17`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00C1FBDA` → [HalpProcGetFeatureBits](../../text/54/HalpProcGetFeatureBits_function_0054E890.md) (function, `0x0054E890`)

### Direct callers
- [HalpProcInitSystem](../../pagelk/B5/HalpProcInitSystem_function_00B5D440.md) at `0x00B5D4BB`

### Static image references
- `0x00C1FB94` → RVA `0x0070B200` (`HalpLoadMicrocode`; read)
- `0x00C1FB9B` → RVA `0x00E008B0` (`.data`; write)
- `0x00C1FBA2` → RVA `0x00A97CF0` (`ArbPreprocessEntry`; read)
- `0x00C1FBA9` → RVA `0x00E008B8` (`.data`; write)
- `0x00C1FBB0` → RVA `0x004D6670` (`HalpMcUpdatePostUpdate`; read)
- `0x00C1FBB7` → RVA `0x00E008C0` (`.data`; write)
- `0x00C1FBBE` → RVA `0x00547A30` (`HalpProcessorPrepareForIdle`; read)
- `0x00C1FBC5` → RVA `0x00E009A0` (`.data`; write)
- `0x00C1FBCC` → RVA `0x00547A80` (`HalpProcessorResumeFromIdle`; read)
- `0x00C1FBD3` → RVA `0x00E009B0` (`.data`; write)
- `0x00C1FBDF` → RVA `0x00FC1C44` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C1FBDA` → [HalpProcGetFeatureBits](../../text/54/HalpProcGetFeatureBits_function_0054E890.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C1FB90  48 83 EC 28                     sub rsp, 0x28
00C1FB94  48 8D 05 65 B6 AE FF            lea rax, [rip - 0x51499b]
00C1FB9B  48 89 05 0E 0D 1E 00            mov qword ptr [rip + 0x1e0d0e], rax
00C1FBA2  48 8D 05 47 81 E7 FF            lea rax, [rip - 0x187eb9]
00C1FBA9  48 89 05 08 0D 1E 00            mov qword ptr [rip + 0x1e0d08], rax
00C1FBB0  48 8D 05 B9 6A 8B FF            lea rax, [rip - 0x749547]
00C1FBB7  48 89 05 02 0D 1E 00            mov qword ptr [rip + 0x1e0d02], rax
00C1FBBE  48 8D 05 6B 7E 92 FF            lea rax, [rip - 0x6d8195]
00C1FBC5  48 89 05 D4 0D 1E 00            mov qword ptr [rip + 0x1e0dd4], rax
00C1FBCC  48 8D 05 AD 7E 92 FF            lea rax, [rip - 0x6d8153]
00C1FBD3  48 89 05 D6 0D 1E 00            mov qword ptr [rip + 0x1e0dd6], rax
00C1FBDA  E8 B1 EC 92 FF                  call 0x14054e890
00C1FBDF  89 05 5F 20 3A 00               mov dword ptr [rip + 0x3a205f], eax
00C1FBE5  33 C0                           xor eax, eax
00C1FBE7  48 83 C4 28                     add rsp, 0x28
00C1FBEB  C3                              ret
00C1FBEC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpProcInitDiscard(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(v_rip + 1969422) = v_rip - 5327259;
    *(unsigned __int64 *)(v_rip + 1969416) = v_rip - 1605305;
    *(unsigned __int64 *)(v_rip + 1969410) = v_rip - 7640391;
    *(unsigned __int64 *)(v_rip + 1969620) = v_rip - 7176597;
    *(unsigned __int64 *)(v_rip + 1969622) = v_rip - 7176531;
    result = HalpProcGetFeatureBits(a1, a2, a3, a4);
    *(unsigned int *)(v_rip + 3809375) = (unsigned int)(result);
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpProcInitDiscard(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint64_t *)(v_rip + 0x1E0D0E) = v_rip - 5327259;
    *(uint64_t *)(v_rip + 0x1E0D08) = v_rip - 1605305;
    *(uint64_t *)(v_rip + 0x1E0D02) = v_rip - 7640391;
    *(uint64_t *)(v_rip + 0x1E0DD4) = v_rip - 7176597;
    *(uint64_t *)(v_rip + 0x1E0DD6) = v_rip - 7176531;
    result = HalpProcGetFeatureBits(a1, a2, a3, a4);
    *(uint32_t *)(v_rip + 0x3A205F) = (uint32_t)(result);
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C1FB90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C1FB90[BB_00C1FB90]
  bb_00C1FBEC[BB_00C1FBEC]
```
