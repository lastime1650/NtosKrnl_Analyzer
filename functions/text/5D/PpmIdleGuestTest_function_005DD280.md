# PpmIdleGuestTest

- RVA: `0x005DD280`–`0x005DD2AB` (길이 `43` bytes)
- VA: `0x00000001405DD280`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005DD29C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005DD28C` → RVA `0x00FC6AD0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DD280  48 83 EC 28                     sub rsp, 0x28
005DD284  33 D2                           xor edx, edx
005DD286  41 83 F8 FF                     cmp r8d, -1
005DD28A  74 17                           je 0x1405dd2a3
005DD28C  48 8B 05 3D 98 9E 00            mov rax, qword ptr [rip + 0x9e983d]
005DD293  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
005DD297  48 85 C0                        test rax, rax
005DD29A  74 07                           je 0x1405dd2a3
005DD29C  E8 2F D8 0D 00                  call 0x1406baad0
005DD2A1  8B D0                           mov edx, eax
005DD2A3  8B C2                           mov eax, edx
005DD2A5  48 83 C4 28                     add rsp, 0x28
005DD2A9  C3                              ret
005DD2AA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmIdleGuestTest(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    if (a3 == -1) goto loc_005DD2A3;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10393661) + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10393661) + 16) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
        a2 = (unsigned int)(result);
    }
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(a2);
}
```

## 5. (Beta) C Style

```c
int64_t PpmIdleGuestTest(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    if (Arg3 == -1) goto loc_005DD2A3;
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x9E983D) + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x9E983D) + 0x10) != 0) {
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
        Arg2 = (uint32_t)(result);
    }
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(Arg2);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DD280&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005DD280[BB_005DD280]
  bb_005DD28C[BB_005DD28C]
  bb_005DD29C[BB_005DD29C]
  bb_005DD2A3[BB_005DD2A3]
  bb_005DD2AA[BB_005DD2AA]
  bb_005DD280 -->|branch| bb_005DD2A3
  bb_005DD280 -->|fallthrough| bb_005DD28C
  bb_005DD28C -->|branch| bb_005DD2A3
  bb_005DD28C -->|fallthrough| bb_005DD29C
  bb_005DD29C -->|flow| bb_005DD2A3
```
