# sub_00891AEC

- RVA: `0x00891AEC`–`0x00891B2A` (길이 `62` bytes)
- VA: `0x0000000140891AEC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007D970`
- 디코드: `12`개 명령, `62/62` bytes 표시
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
- `0x00891AF6` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00891AF0` → [sub_00891C14](Unknown_function_00891C14.md) (`tail-transfer`)
  - `0x00891B00` → [sub_00891C4F](Unknown_function_00891C4F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00891AEC  80 7E 08 00                     cmp byte ptr [rsi + 8], 0
00891AF0  0F 84 1E 01 00 00               je 0x140891c14
00891AF6  48 8B 05 B3 4F 73 00            mov rax, qword ptr [rip + 0x734fb3]
00891AFD  49 39 06                        cmp qword ptr [r14], rax
00891B00  0F 84 49 01 00 00               je 0x140891c4f
00891B06  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00891B0A  49 89 07                        mov qword ptr [r15], rax
00891B0D  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00891B15  C6 00 01                        mov byte ptr [rax], 1
00891B18  33 C0                           xor eax, eax
00891B1A  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
00891B22  4C 8B B4 24 80 00 00 00         mov r14, qword ptr [rsp + 0x80]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00891AEC(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26)
{
    __int64 result;

    *(unsigned __int64 *)(v_r15) = *(unsigned __int64 *)(v_rsi + 16);
    *(unsigned __int8 *)(a26) = 1;
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00891AEC(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, int64_t Arg16, int64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, void *Arg26)
{
    uint8_t *arg26 = (uint8_t *)Arg26;

    int64_t result;

    *(uint64_t *)(local_r15) = *(uint64_t *)(local_rsi + 0x10);
    *(uint8_t *)(arg26) = 1;
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg26` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00891AEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00891AEC[BB_00891AEC]
  bb_00891AF6[BB_00891AF6]
  bb_00891B06[BB_00891B06]
  bb_00891AEC -->|fallthrough| bb_00891AF6
  bb_00891AF6 -->|fallthrough| bb_00891B06
```
