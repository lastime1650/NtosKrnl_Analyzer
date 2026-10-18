# WheaSignalHandlerOverride

- RVA: `0x00661100`–`0x00661133` (길이 `51` bytes)
- VA: `0x0000000140661100`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `16`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00661122` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0066110F` → RVA `0x00EEFA50` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00661100  48 83 EC 28                     sub rsp, 0x28
00661104  45 33 C0                        xor r8d, r8d
00661107  83 F9 12                        cmp ecx, 0x12
0066110A  77 1E                           ja 0x14066112a
0066110C  48 63 C1                        movsxd rax, ecx
0066110F  48 8D 0D 3A E9 88 00            lea rcx, [rip + 0x88e93a]
00661116  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0066111A  48 85 C0                        test rax, rax
0066111D  74 0B                           je 0x14066112a
0066111F  48 8B CA                        mov rcx, rdx
00661122  E8 A9 99 05 00                  call 0x1406baad0
00661127  44 8A C0                        mov r8b, al
0066112A  41 8A C0                        mov al, r8b
0066112D  48 83 C4 28                     add rsp, 0x28
00661131  C3                              ret
00661132  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheaSignalHandlerOverride(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = 0;
    if (a1 > 18) goto loc_0066112A;
    result = *(unsigned __int64 *)(v_rip + 8972602 + (int)(a1) * 8);
    if (*(unsigned __int64 *)(v_rip + 8972602 + (int)(a1) * 8) != 0) {
        a1 = a2;
        result = guard_dispatch_icall(a1, a2, a3, a4);
        a3 = (unsigned __int8)(result);
    }
    v_rsp = (v_rsp) + (40);
    return (unsigned __int8)(a3);
}
```

## 5. (Beta) C Style

```c
int64_t WheaSignalHandlerOverride(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg3 = 0;
    if (Arg1 > 18) goto loc_0066112A;
    result = *(uint64_t *)(v_rip + 0x88E93A + (int32_t)(Arg1) * 8);
    if (*(uint64_t *)(v_rip + 0x88E93A + (int32_t)(Arg1) * 8) != 0) {
        Arg1 = Arg2;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
        Arg3 = (uint8_t)(result);
    }
    local_rsp = (local_rsp) + (40);
    return (uint8_t)(Arg3);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00661100&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00661100[BB_00661100]
  bb_0066110C[BB_0066110C]
  bb_0066111F[BB_0066111F]
  bb_0066112A[BB_0066112A]
  bb_00661132[BB_00661132]
  bb_00661100 -->|branch| bb_0066112A
  bb_00661100 -->|fallthrough| bb_0066110C
  bb_0066110C -->|branch| bb_0066112A
  bb_0066110C -->|fallthrough| bb_0066111F
  bb_0066111F -->|flow| bb_0066112A
```
