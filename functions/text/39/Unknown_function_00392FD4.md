# sub_00392FD4

- RVA: `0x00392FD4`–`0x00392FF7` (길이 `35` bytes)
- VA: `0x0000000140392FD4`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00080D94`
- 디코드: `7`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00392FE9` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00392FF5` → [sub_00392FF7 + 0xD](Unknown_function_00392FF7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00392FD4  F0 0F BA 37 12                  lock btr dword ptr [rdi], 0x12
00392FD9  48 89 6F 68                     mov qword ptr [rdi + 0x68], rbp
00392FDD  F0 0F BA 77 78 09               lock btr dword ptr [rdi + 0x78], 9
00392FE3  F0 48 83 63 30 00               lock and qword ptr [rbx + 0x30], 0
00392FE9  83 3D 30 3D C3 00 00            cmp dword ptr [rip + 0xc33d30], 0
00392FF0  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00392FF5  74 0D                           je 0x140393004
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00392FD4(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    *(unsigned __int64 *)(v_rdi + 104) = v_rbp;
}
```

## 5. (Beta) C Style

```c
void sub_00392FD4(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6)
{
    *(uint64_t *)(local_rdi + 0x68) = local_rbp;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00392FD4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00392FD4[BB_00392FD4]
```
