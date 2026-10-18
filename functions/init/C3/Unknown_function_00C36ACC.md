# sub_00C36ACC

- RVA: `0x00C36ACC`–`0x00C36AE9` (길이 `29` bytes)
- VA: `0x0000000140C36ACC`
- 실행 섹션: `INIT`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C9720`
- 디코드: `5`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C36ACF` → [KcsanInitSystem](../../text/5A/KcsanInitSystem_function_005AF2A0.md) (function, `0x005AF2A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C36AD4` → RVA `0x00FCEC69` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C36ACF` → [KcsanInitSystem](../../text/5A/KcsanInitSystem_function_005AF2A0.md) (`INIT` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00C36AE3` → [sub_00C36AE9 + 0x20B](Unknown_function_00C36AE9.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00C36ACC  41 8B CE                        mov ecx, r14d
00C36ACF  E8 CC 87 97 FF                  call 0x1405af2a0
00C36AD4  40 38 35 8E 81 39 00            cmp byte ptr [rip + 0x39818e], sil
00C36ADB  4C 8B B4 24 F0 00 00 00         mov r14, qword ptr [rsp + 0xf0]
00C36AE3  0F 84 0B 02 00 00               je 0x140c36cf4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00C36ACC(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30)
{
    __int64 result;

    result = KcsanInitSystem((unsigned int)((unsigned int)(v_r14)), a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00C36ACC(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, int64_t Arg30)
{
    int64_t result;

    result = KcsanInitSystem((uint32_t)((uint32_t)(local_r14)), Arg2, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C36ACC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C36ACC[BB_00C36ACC]
```
