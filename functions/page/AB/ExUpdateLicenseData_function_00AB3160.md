# ExUpdateLicenseData

- RVA: `0x00AB3160`–`0x00AB3197` (길이 `55` bytes)
- VA: `0x0000000140AB3160`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `15`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AB3167` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00AB3185` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AB3190` → [SLUpdateLicenseDataInternal](../7C/SLUpdateLicenseDataInternal_function_007C9C04.md) (function, `0x007C9C04`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AB3179` → RVA `0x00FD84B0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AB3167` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x00AB3185` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB3160  48 83 EC 28                     sub rsp, 0x28
00AB3164  44 8B C9                        mov r9d, ecx
00AB3167  E8 84 B0 84 FF                  call 0x1402fe1f0
00AB316C  4C 8B C2                        mov r8, rdx
00AB316F  41 8B D1                        mov edx, r9d
00AB3172  48 8B 88 68 03 00 00            mov rcx, qword ptr [rax + 0x368]
00AB3179  48 8B 05 30 53 52 00            mov rax, qword ptr [rip + 0x525330]
00AB3180  48 85 C0                        test rax, rax
00AB3183  74 0B                           je 0x140ab3190
00AB3185  E8 46 79 C0 FF                  call 0x1406baad0
00AB318A  48 83 C4 28                     add rsp, 0x28
00AB318E  C3                              ret
00AB318F  CC                              int3
00AB3190  E8 6F 6A D1 FF                  call 0x1407c9c04
00AB3195  EB F3                           jmp 0x140ab318a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExUpdateLicenseData(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, (unsigned int)(a1));
    if (*(unsigned __int64 *)(v_rip + 5395248) == 0) goto loc_00AB3190;
    result = guard_dispatch_icall(*(unsigned __int64 *)(result + 872), (unsigned int)((unsigned int)((unsigned int)(a1))), a2, (unsigned int)(a1));
loc_00AB318A:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00AB3190:
    result = SLUpdateLicenseDataInternal(*(unsigned __int64 *)(result + 872), (unsigned int)((unsigned int)((unsigned int)(a1))), a2, (unsigned int)(a1));
    goto loc_00AB318A;
}
```

## 5. (Beta) C Style

```c
int64_t ExUpdateLicenseData(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, a3, (uint32_t)(Arg1));
    if (*(uint64_t *)(v_rip + 0x525330) == 0) goto loc_00AB3190;
    result = guard_dispatch_icall(*(uint64_t *)(result + 0x368), (uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, (uint32_t)(Arg1));
loc_00AB318A:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00AB3190:
    result = SLUpdateLicenseDataInternal(*(uint64_t *)(result + 0x368), (uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, (uint32_t)(Arg1));
    goto loc_00AB318A;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB3160&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB3160[BB_00AB3160]
  bb_00AB3185[BB_00AB3185]
  bb_00AB318A[BB_00AB318A]
  bb_00AB318F[BB_00AB318F]
  bb_00AB3190[BB_00AB3190]
  bb_00AB3160 -->|branch| bb_00AB3190
  bb_00AB3160 -->|fallthrough| bb_00AB3185
  bb_00AB3185 -->|flow| bb_00AB318A
  bb_00AB318F -->|flow| bb_00AB3190
  bb_00AB3190 -->|branch| bb_00AB318A
```
