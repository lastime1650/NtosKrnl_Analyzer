# sub_002436D0

- RVA: `0x002436D0`–`0x00243729` (길이 `89` bytes)
- VA: `0x00000001402436D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061BE4`
- 디코드: `22`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x002436D7` → [sub_0024376F + 0x88](Unknown_function_0024376F.md) (`tail-transfer`)
  - `0x002436F8` → [sub_0024376F](Unknown_function_0024376F.md) (`tail-transfer`)
  - `0x00243723` → [sub_0024382B](Unknown_function_0024382B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002436D0  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
002436D3  0F BA E0 1A                     bt eax, 0x1a
002436D7  0F 83 1A 01 00 00               jae 0x1402437f7
002436DD  4C 8B 03                        mov r8, qword ptr [rbx]
002436E0  49 C1 E8 20                     shr r8, 0x20
002436E4  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
002436E7  41 81 E0 FF 03 00 00            and r8d, 0x3ff
002436EE  45 03 C6                        add r8d, r14d
002436F1  41 8B D0                        mov edx, r8d
002436F4  0F BA E0 1A                     bt eax, 0x1a
002436F8  73 75                           jae 0x14024376f
002436FA  48 8B 03                        mov rax, qword ptr [rbx]
002436FD  48 C1 E2 20                     shl rdx, 0x20
00243701  48 8B CA                        mov rcx, rdx
00243704  48 33 C8                        xor rcx, rax
00243707  48 B8 FF FF FF FF 00 FC FF FF   movabs rax, 0xfffffc00ffffffff
00243711  48 23 C8                        and rcx, rax
00243714  48 33 CA                        xor rcx, rdx
00243717  48 89 0B                        mov qword ptr [rbx], rcx
0024371A  40 F6 C5 04                     test bpl, 4
0024371E  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
00243723  0F 85 02 01 00 00               jne 0x14024382b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002436D0(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    a3 = (*(unsigned __int64 *)(v_rbx)) >> (32);
    a3 = (unsigned int)((a3) & (0x3FFULL));
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r14)));
    a2 = ((unsigned int)((unsigned int)(a3))) << (32);
    a1 = (a2) ^ (*(unsigned __int64 *)(v_rbx));
    a1 = (a1) & (*(unsigned __int64 *)(v_rbx));
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(v_rbx) = a1;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002436D0(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6)
{
    Arg3 = (*(uint64_t *)(local_rbx)) >> (32);
    Arg3 = (uint32_t)((Arg3) & (0x3FFULL));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_r14)));
    Arg2 = ((uint32_t)((uint32_t)(Arg3))) << (32);
    Arg1 = (Arg2) ^ (*(uint64_t *)(local_rbx));
    Arg1 = (Arg1) & (*(uint64_t *)(local_rbx));
    Arg1 = (Arg1) ^ (Arg2);
    *(uint64_t *)(local_rbx) = Arg1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002436D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002436D0[BB_002436D0]
  bb_002436DD[BB_002436DD]
  bb_002436FA[BB_002436FA]
  bb_002436D0 -->|fallthrough| bb_002436DD
  bb_002436DD -->|fallthrough| bb_002436FA
```
